from flask import Blueprint, render_template, request
import random
from collections import Counter

bp = Blueprint('page_100', __name__)

# --- POKER ENGINE ---

RANKS = '23456789TJQKA'
SUITS = 'shdc'  # spades, hearts, diamonds, clubs
RANK_VAL = {r: i for i, r in enumerate(RANKS, 2)}


def get_deck():
    """Generates a shuffled deck of 52 cards."""
    deck = [r + s for r in RANKS for s in SUITS]
    random.shuffle(deck)
    return deck


def eval_hand(cards):
    """
    Returns a score tuple: (Hand_Type_Score, [Tie_Breaker_Cards])
    8=StrFlush, 7=Quads, 6=FullHouse, 5=Flush, 4=Straight,
    3=Trips, 2=TwoPair, 1=Pair, 0=HighCard
    """
    # Parse cards
    ranks = sorted([RANK_VAL[c[0]] for c in cards], reverse=True)
    suits = [c[1] for c in cards]
    count = Counter(ranks)
    counts = count.most_common()  # e.g. [(14, 2), (10, 1)...] (Pair of Aces)

    is_flush = False
    flush_suit = Counter(suits).most_common(1)[0]
    if flush_suit[1] >= 5:
        is_flush = True
        # Filter only flush cards for tie breaking
        flush_ranks = sorted(
            [RANK_VAL[c[0]] for c in cards if c[1] == flush_suit[0]],
            reverse=True)

    # Check Straight
    unique_ranks = sorted(list(set(ranks)), reverse=True)
    straight_high = None
    # Special Ace Low check (A, 5, 4, 3, 2)
    if {14, 5, 4, 3, 2}.issubset(set(unique_ranks)):
        straight_high = 5
    for i in range(len(unique_ranks) - 4):
        if unique_ranks[i] - unique_ranks[i + 4] == 4:
            straight_high = unique_ranks[i]
            break

    # 1. Straight Flush
    if is_flush and straight_high:
        # Simplified check (doesn't perfectly handle Royal Flush vs lower Straight Flush overlap perfectly in tiny code, but good enough)
        return (8, straight_high)

    # 2. Four of a Kind
    if counts[0][1] == 4: return (7, counts[0][0], counts[1][0])

    # 3. Full House
    if counts[0][1] == 3 and counts[1][1] >= 2: return (
    6, counts[0][0], counts[1][0])

    # 4. Flush
    if is_flush: return (5, flush_ranks[:5])

    # 5. Straight
    if straight_high: return (4, straight_high)

    # 6. Three of a Kind
    if counts[0][1] == 3: return (3, counts[0][0], ranks[:2])

    # 7. Two Pair
    if counts[0][1] == 2 and counts[1][1] == 2: return (
    2, counts[0][0], counts[1][0], counts[2][0])

    # 8. Pair
    if counts[0][1] == 2:
        kickers = [r for r in ranks if r != counts[0][0]]
        return (1, counts[0][0], kickers[:3])

    # 9. High Card
    return (0, ranks[:5])


def describe_hand(score_tuple):
    types = ["High Card", "Pair", "Two Pair", "Three of a Kind", "Straight",
             "Flush", "Full House", "Quads", "Straight Flush"]
    return types[score_tuple[0]]


# --- ROUTES ---

@bp.route('/poker-sim', methods=['GET', 'POST'])
def show():
    # To keep this stateless (no database), we pass the deck state in a hidden form field.

    if request.method == 'POST':
        # RECONSTRUCT GAME STATE
        state_str = request.form.get('gamestate')
        action = request.form.get('action')  # 'play' or 'fold'

        full_deck = state_str.split(',')

        # Re-deal exactly as before
        user_hand = full_deck[0:2]
        bot_hands = [full_deck[2:4], full_deck[4:6], full_deck[6:8],
                     full_deck[8:10], full_deck[10:12]]
        community = full_deck[12:17]  # Flop(3) + Turn(1) + River(1)

        # Evaluate Winner
        best_score = (-1, [])
        winner_idx = -1  # 0 is user, 1-5 are bots

        # Check User
        user_score = eval_hand(user_hand + community)
        best_score = user_score
        winner_idx = 0

        # Check Bots
        bot_results = []
        for i, hand in enumerate(bot_hands):
            score = eval_hand(hand + community)
            bot_results.append(
                {'id': i + 1, 'hand': hand, 'desc': describe_hand(score)})
            if score > best_score:
                best_score = score
                winner_idx = i + 1

        result_msg = ""
        if action == 'fold':
            result_msg = f"You folded. Bot {winner_idx} would have won with {describe_hand(best_score)}." if winner_idx != 0 else f"You folded, but you would have won with {describe_hand(best_score)}!"
        else:
            result_msg = "YOU WON!" if winner_idx == 0 else f"Bot {winner_idx} Wins!"

        return render_template('page_100.html',
                               mode='result',
                               user_hand=user_hand,
                               community=community,
                               bot_results=bot_results,
                               winner_idx=winner_idx,
                               user_desc=describe_hand(user_score),
                               result_msg=result_msg)

    else:
        # INITIAL DEAL
        deck = get_deck()
        # Create a string representation to pass to HTML
        gamestate = ",".join(deck)

        user_hand = deck[0:2]
        # We don't show bots or community cards yet

        return render_template('page_100.html',
                               mode='deal',
                               user_hand=user_hand,
                               gamestate=gamestate)