from collections import deque
import sys

data = open(sys.argv[1]).read().strip().split('\n')
grid = [[ch for ch in row] for row in data]

def energy(r, c, dr, dc):
    
    beams = set()    
    initial = [(r, c, dr, dc)]
    q = deque(initial)

    def add_beam(r,c,dr,dc):
        if (r,c,dr,dc) not in beams:
            beams.add((r,c,dr,dc))
            q.append((r,c,dr,dc))

    while q:
        r, c, dr, dc = q.popleft()
        r += dr
        c += dc

        if not(0<=r<len(grid) and 0<=c<len(grid[0])):
            continue

        ch = grid[r][c]

        if ch == '.' or (ch == '-' and dc != 0) or (ch == '|' and dr != 0):
            add_beam(r,c,dr,dc)

        elif ch == '/':
            dr, dc = -dc , -dr
            add_beam(r,c,dr,dc)
        
        elif ch == '\\':
            dr, dc = dc , dr
            add_beam(r,c,dr,dc)

        else:
            for dr,dc in [(1,0),(-1,0)] if ch == '|' else [(0,1),(0,-1)]:
                add_beam(r,c,dr,dc)

    energized = {(r,c) for (r,c,_,_) in beams}
    return len(energized)

ans = 0
for r in range(len(grid)):
    ans = max(ans, energy(r, -1, 0, 1))
    ans = max(ans, energy(r, len(grid[0]), 0, -1))
    
for c in range(len(grid)):
    ans = max(ans, energy(-1, c, 1, 0))
    ans = max(ans, energy(len(grid), c, -1, 0))

print(ans)


