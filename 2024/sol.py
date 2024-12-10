import sys


D = open(sys.argv[1]).read().strip().split('\n')

grid = [[int(x) for x in row] for row in D]

X = len(grid)
Y = len(grid[0])

def bfs(grid,pos):
	hikes = 0
	dirs = [(0,1),(1,0),(-1,0),(0,-1)]
	q = [pos]
	visited = set()
	while q:
		pos = q.pop(0)
		if pos in visited:
			continue
		visited.add(pos)
		x,y = pos
		slope =  grid[x][y]
		if slope == 9:
			hikes += 1
			continue
		for dx,dy in dirs:
			xx,yy = x+dx, y+dy
			if xx >= 0 and xx < X and yy >= 0 and yy < Y and grid[xx][yy] - slope == 1:
				q.append((xx,yy))
	return hikes

p1 = 0
for x in range(X):
	for y in range(Y):
		if grid[x][y] == 0:
			p1 += bfs(grid,(x,y))

print(p1)
