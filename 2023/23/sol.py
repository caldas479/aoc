import sys
sys.setrecursionlimit(10000)
data = open(sys.argv[1]).read().strip().split('\n')
grid = [[ch for ch in row] for row in data]
R, C = len(grid), len(grid[0])
dirs = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
target = None
for c in range(C):
    if grid[R-1][c] == ".":
        target = (R-1,c)

def is_valid(r, c):
    return 0 <= r < R and 0 <= c < C and grid[r][c] != "#"

def dfs(r, c, visited):
    visited.add((r, c))
    if (r, c) == target:
        return 1
    
    max_path_length = 0
    if grid[r][c] in dirs:
        dr,dc = dirs[grid[r][c]]
        nr, nc = r + dr, c + dc
        if is_valid(nr, nc) and (nr, nc) not in visited:
                path_length = dfs(nr, nc, visited)
                max_path_length = max(max_path_length, path_length)
    else:
        for dr, dc in dirs.values():
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc) and (nr, nc) not in visited:
                path_length = dfs(nr, nc, visited)
                max_path_length = max(max_path_length, path_length)

    visited.remove((r, c))  # Backtrack

    return max_path_length + 1

longest_hike = 0
for c in range(C):
    if grid[0][c] == '.':
        longest_hike = max(longest_hike, dfs(0, c, set()))

print(longest_hike)

