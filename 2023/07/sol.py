from collections import defaultdict
import sys

lines = open(sys.argv[1]).read().strip().split('\n')
hands = []
values = {'A': 14, 'K': 13, 'Q':12, 'J': 1, 'T': 10}

for line in lines:
    hand, bid = line.split(' ')
    cards = {}
    h = []
    for card in hand:
        if card in values:
            card = values[card]
        card = int(card)
        if card not in cards:
            cards[card] = 0
        cards[card] += 1
        h += [card]     
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
    hands += [(t,h,int(bid))]

sorted_hands = sorted(hands, key=lambda x: (x[0],x[1]))

ans = 0
for i,hand in enumerate(sorted_hands):
    ans += (i+1)*hand[2]

print(ans)