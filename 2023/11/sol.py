import sys

data = open(sys.argv[1]).read().strip().split('\n')
grid = [[ch for ch in row] for row in data]

MAX_COL = len(grid[0])
MAX_ROW = len(grid)

empty_rows = []
for r in range(MAX_ROW) :
    empty = True
    for c in range(MAX_COL):
        if grid[r][c] == '#':
            empty = False
    if empty:
        empty_rows.append(r)

empty_cols = []
for c in range(MAX_COL):
    empty = True
    for r in range(MAX_ROW):
        if grid[r][c] == '#':
            empty = False
    if empty:
        empty_cols.append(c)

# Doesn't work without real expansion of the grid
# For part2 would take a lot of time
def bfs_solution():
    def get_nbrs(pos):
        nbrs = []
        i, j = pos
        dirs = [(1,0),(0,1),(-1,0),(0,1)]
        for di, dj in dirs:
            ii,jj = i + di, j + dj
            if not(0<=ii<MAX_ROW and 0<=jj<MAX_COL):
                continue
            nbrs.append((ii,jj))
        return nbrs

    distances = {}
    def bfs(pos):
        visited = set()
        q = [(pos,0)]
        while q:
            p, d = q.pop(0)
            if p in visited:
                continue
            visited.add(p)
            nbrs = get_nbrs(p)
            for nbr in nbrs:
                if nbr in visited:
                    continue
                if grid[nbr[0]][nbr[1]] == "#":
                    if not ((pos,(nbr[0],nbr[1])) in distances or ((nbr[0],nbr[1]),pos) in distances):
                        distances[(pos,(nbr[0],nbr[1]))] = d + 1
                q.append((nbr,d+1))

    galaxies = [(r,c) for c in range(MAX_COL) for r in range(MAX_ROW) if grid[r][c] == "#"]
    while galaxies:
        bfs(galaxies.pop(0))

    print(sum(distances.values()))

def opt_solution():
    galaxies = [(r,c) for c in range(MAX_COL) for r in range(MAX_ROW) if grid[r][c] == "#"]
    ans = 0
    for i,(r,c) in enumerate(galaxies):
        for j in range(i,len(galaxies)):
            rr,cc = galaxies[j]
            ans += abs(rr-r) + abs(cc-c)
            for er in empty_rows:
                if min(r,rr)<= er <= max(r,rr):
                    ans += int(10**6-1)
            for ec in empty_cols:
                if min(c,cc)<= ec <= max(c,cc):
                    ans += int(10**6-1)
    
    print(ans)

opt_solution()