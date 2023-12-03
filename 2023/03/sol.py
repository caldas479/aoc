from collections import defaultdict
import sys

data = open(sys.argv[1]).read().strip()
lines = data.split('\n')
d = [[c for c in line] for line in lines]
ans = 0
MAX_ROW = len(d)
MAX_COL = len(d[0])
nums = defaultdict(list)
for r in range(len(d)):
    n = 0
    adjacent = False
    gears = set()
    for c in range(len(d[r])):
        if d[r][c].isdigit():
            n = n*10 + int(d[r][c])
            for rr in (-1,0,1):
                for cc in (-1,0,1):
                    if 0 <= r + rr < MAX_ROW and 0 <= c + cc < MAX_COL:
                        ch = d[r+rr][c+cc]
                        if ch != '.' and not ch.isdigit():
                            adjacent = True
                        if ch == '*':
                            gears.add((r+rr,c+cc))
        elif n > 0:
            for gear in gears:
                nums[gear].append(n)
            #if adjacent:
                #ans += n
            n = 0
            adjacent = False
            gears = set()

for k,v in nums.items():
    if len(v) == 2:
        ans += v[0]*v[1]
            
print(ans)



