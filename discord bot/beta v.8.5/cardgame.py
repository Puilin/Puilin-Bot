
def fresh_deck():
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"}
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((suit, rank))
    import random
    random.shuffle(deck)
    return deck

def hit(deck):
    if deck == []:
        deck = fresh_deck()
    return (deck[0], deck[1:])

def count_score(cards):
    score = 0
    num_of_ace = 0
    for card in cards:
        if card[1] in [2,3,4,5,6,7,8,9,10]:
            score += card[1]
        elif card[1] in ["J", "Q", "K"]:
            score += 10
        else: #'A'
            score += 11
            num_of_ace += 1
    while score > 21 and num_of_ace >= 1:
        score -= 10
        num_of_ace -= 1
    return score
