from collections import defaultdict
import sys

lines = open(sys.argv[1]).read().strip().split('\n')
hands = []

sameTypeHands = defaultdict(list)

values = {'A': 14, 'K': 13, 'Q':12, 'J': 11, 'T': 10}

def count_cards(hand):
    count = set()
    for k, v in cards.items():
        count.add(v)
    return count

for line in lines:
    hand, bid = line.split(' ')
    cards = {}
    val = 0
    for card in hand:
        if card in values:
            card = values[card]
        if card not in cards:
            cards[card] = 0
        cards[card] += 1
    print(cards)
    count = count_cards(cards)
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
    cards['bid'] = int(bid) 
    cards['type'] = t
    cards['val'] = val
    hands += [cards]

sorted_hands = sorted(hands, key=lambda x: (x['type'], x['val']))

ans = 0
for i,hand in enumerate(sorted_hands):
    ans += (i+1)*hand['bid']

print(ans)