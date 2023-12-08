from collections import defaultdict
import sys

lines = open(sys.argv[1]).read().strip().split('\n')
hands = []
values = {'A': "13", 'K': "12", 'Q':"11", 'J': "0", 'T': "10"}

def replace(hand):
    if hand == "":
        return [""]
    return [ x + y for x in ("23456789TQKA" if hand[0] == "J" else hand[0]) for y in replace(hand[1:])]

def classify(hand):
    cards = {}
    for card in hand:
        if card not in cards:
            cards[card] = 0
        cards[card] += 1
    t = 1
    count = cards.values()
    if len(cards) == 1:
        t = 7
    elif len(cards) == 2:     
        t = 6 if 4 in count else 5
    elif len(cards) == 3:
        t = 4 if 3 in count else 3
    elif len(cards) == 4:
        t = 2
    else:
        t = 1 
    return t

def strength(hand):
    return (max(map(classify, replace(hand))), [values.get(card,card) for card in hand])

for line in lines:
    hand, bid = line.split(' ')
    hands += [(hand,int(bid))]

sorted_hands = sorted(hands, key=lambda hand: strength(hand[0]))

ans = 0
for i,hand in enumerate(sorted_hands):
    ans += (i+1)*hand[1]

print(ans)