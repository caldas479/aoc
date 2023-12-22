import sys
from heapq import heappush, heappop

data = open(sys.argv[1]).read().strip().split('\n')

grid = [[int(ch) for ch in row] for row in data]


q = [(0,0,0,0,0,0)]
seen = set()

while q:
	h,r,c,dr,dc,n = heappop(q)
	if r == len(grid)-1 and c == len(grid[0])-1:
		print(h)
		break

	if (r,c,dr,dc,n) in seen:
		continue

	seen.add((r,c,dr,dc,n))

	if n<10 and (dr,dc) != (0,0):
		rr = r+dr
		cc = c+dc
		if 0<=rr<len(grid) and 0<=cc<len(grid[0]):
			heappush(q,(h+grid[rr][cc],rr,cc,dr,dc,n+1))
	if n==0 or n>=4:
		for drr, dcc in [(0,1),(1,0),(0,-1),(-1,0)]:
			if (drr,dcc) != (dr,dc) and (drr,dcc) != (-dr,-dc):
				rr = r+drr
				cc = c+dcc
				if 0<=rr<len(grid) and 0<=cc<len(grid[0]):
					heappush(q,(h+grid[rr][cc],rr,cc,drr,dcc,1))

