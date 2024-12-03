from collections import defaultdict
import sys

data = open(sys.argv[1]).read().split('\n')
grid = [[c for c in row] for row in data]

def rotate(grid):
    rows = len(grid)
    columns = len(grid[0])
    rotated = [['0'] * rows for _ in range(columns)]
    for i in range(rows):
        for j in range(columns):
            rotated[j][rows - 1 - i] = grid[i][j]
    return rotated

def tilt(grid):
    for c in range(len(grid[0])):
        repeat = 1
        while(repeat):
            repeat = 0
            for r in range(1,len(grid)):
                if grid[r][c] == 'O' and grid[r-1][c] == '.':
                    grid[r-1][c] = 'O'
                    grid[r][c] = '.'
            for r in range(1,len(grid)):
                if grid[r][c] == 'O' and grid[r-1][c] == '.':
                    repeat = 1
    return grid

def score(grid):
    score = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'O':
                score += len(grid)-r
    return score

scores = defaultdict(list)
t = 0
ans = 0
while (t<10**9):
    t+=1
    for c in range(4):
        grid = tilt(grid)
        if t == 1 and c == 0:
            print(score(grid))
        grid = rotate(grid)

    s = score(grid)
    scores[s].append(t)

    ts = scores[s]

    if len(ts) >= 6:
        cycle_len = ts[-1] - ts[-2]
        if cycle_len == ts[-2] - ts[-3]:
            amt = (10**9 - t)//cycle_len
            t += amt*cycle_len

print(score(grid))
