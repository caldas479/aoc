import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'in.txt'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

grid = [[ord(x) for x in line] for line in lines]
S = ()
E = ()

queue = []

for r in range(len(grid)):
	for c in range(len(grid[0])):
		if grid[r][c] == ord('S'):
			grid[r][c] = ord('a')
			S = (r,c)
			queue.append((S,0))
		elif grid[r][c] == ord('E'):
			grid[r][c] = ord('z')
			E = (r,c)
		if grid[r][c] == ord('a'):
			queue.append(((r,c),0))

DIR =[(1,0),(0,1),(-1,0),(0,-1)]
vis = set()

while queue:
	p, d = queue.pop(0)
	r = p[0]
	c = p[1]
	if (r,c) in vis:
		continue
	if (r,c) == E:
		print(d)
	vis.add((r,c))
	for dir in DIR:
		dr = r+dir[0]
		dc = c+dir[1]
		if (0 <= dr < len(grid) and 0 <= dc < len(grid[0]) and grid[dr][dc] - grid[r][c] <= 1):
			queue.append(((dr,dc),d+1))





