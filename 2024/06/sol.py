import sys

def loop(grid,x,y):
	pos = (x,y)
	visited = set()
	dir = (-1,0)
	while True:
		
		visited.add((pos,dir))

		dx,dy = dir
		xx, yy = pos[0] + dx, pos[1] + dy
		if xx < 0 or yy < 0 or xx >= X or yy >= Y:
			return False

		if grid[xx][yy] == "#":
			dir = (dy, -dx)
			continue
		pos=(xx,yy)

		if (pos,dir) in visited:
			return True

D = open(sys.argv[1]).read().strip().split('\n')

X = len(D)
Y = len(D[0])

pos = ()
for x in range(X):
	for y in range(Y):
		if D[x][y] not in "#.":
			pos = (x,y)
			break
	if len(pos) > 0:
		break

grid = [[c for c in row] for row in D]
p2 = 0
for xo in range(X):
	for yo in range(Y):
		if grid[xo][yo] != ".":
			continue
		grid[xo][yo] = "#"
		if loop(grid,x,y):
			p2 += 1
		grid[xo][yo] = "."
print(p2)


