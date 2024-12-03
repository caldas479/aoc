import sys
import numpy as np

data = open(sys.argv[1]).read().split('\n\n')

def get_mirror(grid):
    for r in range(1,len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        
        if sum(sum(0 if a == b else 1 for a, b in zip(ra,rb)) for ra, rb in zip(above,below))==1:
            return r
    return 0

ans = 0
for pattern in data:
    grid = pattern.split()
    ans += get_mirror(grid)*100
    grid_transpose = list(zip(*grid))
    ans += get_mirror(grid_transpose)

print(ans)
    