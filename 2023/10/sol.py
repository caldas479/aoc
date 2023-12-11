import sys

data = open(sys.argv[1]).read().strip().split('\n')
grid = [[ch for ch in row] for row in data]

MAX_COL = len(grid[0])
MAX_ROW = len(grid)

NBRS = {
    "|": [(1,0),(-1,0)],
    "-": [(0,1),(0,-1)],
    "L": [(-1,0),(0,1)],
    "J": [(-1,0),(0,-1)],
    "7": [(1,0),(0,-1)],
    "F": [(1,0),(0,1)],
    ".": []
}

initial = ()
for i in range(MAX_ROW):
    for j in range(MAX_COL):
        if grid[i][j] == 'S':
            initial = (i,j)
            grid[i][j] = 'F' # CHEAT
            break

def get_nbrs(pos):
    nbrs = []
    i, j = pos
    for di, dj in list(NBRS[grid[i][j]]):
        ii,jj = i + di, j + dj
        if not(0<=ii<MAX_ROW and 0<=jj<MAX_COL):
            continue
        nbrs.append((ii,jj))
    return nbrs

def bfs(pos):
    visited = set()
    distances = {}
    q = [(pos,0)]
    while q:
        p, d = q.pop(0)
        if p in visited:
            continue
        visited.add(p)
        distances[p] = d
        nbrs = get_nbrs(p)
        for nbr in nbrs:
            if nbr in visited:
                continue
            q.append((nbr,d+1))
    return max(distances.values())

print(bfs(initial))