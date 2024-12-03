import sys
data = open(sys.argv[1]).read().strip().split('\n')

def next_value(seq):
    l = []
    for i in range(len(seq) - 1):
        l.append(seq[i+1] - seq[i])
    if all(n == 0 for n in l):
        return seq[0]
    return seq[0] - next_value(l)

ans = 0
for seq in data:
    seq = [int(n) for n in seq.split()]
    ans += next_value(seq)

print(ans)