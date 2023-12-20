import sys

data = open(sys.argv[1]).read().strip().split('\n')

def hash(s):
    curr = 0
    for ch in s:
        curr += ord(ch)
        curr *= 17
        curr %= 256
    return curr
ans = 0
for step in data[0].split(','):
    ans += hash(step)

print(ans)