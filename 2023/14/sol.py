import sys

data = open(sys.argv[1]).read().split('\n')
grid = [[c for c in row] for row in data]
R = len(grid)
C = len(grid[0])
for c in range(C):
    repeat = 1
    while(repeat):
        repeat = 0
        for r in range(1,R):
            if grid[r][c] == 'O' and grid[r-1][c] == '.':
                grid[r-1][c] = 'O'
                grid[r][c] = '.'
        for r in range(1,R):
            if grid[r][c] == 'O' and grid[r-1][c] == '.':
                repeat = 1

ans = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == 'O':
            ans += R-r

print(ans)