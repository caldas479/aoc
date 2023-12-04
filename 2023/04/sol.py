import sys

data = open(sys.argv[1]).read().strip().split('\n')
ans = 0

copies = {}
for id, card in enumerate(data):
    card = card.split(':')
    card_lists = card[1].split('|')
    wining_nums = card_lists[0].split()
    nums = card_lists[1].split()
    w_nums = set()
    for n in wining_nums:
        w_nums.add(int(n))
    c = 0
    matching = 0
    for n in nums:
        if int(n) in w_nums:
            matching += 1
            if c == 0:
                c = 1
            else:
                c = c*2

    #P2
    if id not in copies:
        copies[id] = 0
    # Add original
    copies[id] += 1
    for i in range(1,matching+1):
        if id + i in copies:
            copies[id+i] += copies[id]
        else:
            copies[id+i] = copies[id]
    ans += c

print(ans)
ans = 0
for k,v in copies.items():
    ans += v
print(ans)
