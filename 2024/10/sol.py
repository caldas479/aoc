import sys

D = open(sys.argv[1]).read().strip().split('\n')

grid = [[int(x) for x in row] for row in D]

X = len(grid)
Y = len(grid[0])

def bfs(grid, pos, use_visited):
    hikes = 0
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    q = [pos]
    visited = set() if use_visited else None

    while q:
        pos = q.pop(0)
        if use_visited and pos in visited:
            continue
        if use_visited:
            visited.add(pos)

        x, y = pos
        slope = grid[x][y]
        if slope == 9:
            hikes += 1
            continue

        for dx, dy in dirs:
            xx, yy = x + dx, y + dy
            if 0 <= xx < len(grid) and 0 <= yy < len(grid[0]) and grid[xx][yy] - slope == 1:
                q.append((xx, yy))

    return hikes


p1 = p2 = 0
for x in range(X):
    for y in range(Y):
        if grid[x][y] == 0:
            p1 += bfs(grid, (x, y), use_visited=True)
            p2 += bfs(grid, (x, y), use_visited=False)

print(p1)
print(p2)
