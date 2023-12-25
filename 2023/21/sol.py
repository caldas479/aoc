import sys

data = open(sys.argv[1]).read().strip().split('\n')

grid = [[ch for ch in row] for row in data]

R = len(grid)
C = len(grid[0])

q = []

for r in range(R):
	for c in range(C):
		if grid[r][c] == 'S':
			q.append(((r,c),0))
			break
S = {}
while q:
	pos, steps = q.pop(0)
	if steps > 64:
		break
	if pos in S:
		S[pos]=steps
		continue
	S[pos]=steps
	for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
		r,c=pos
		rr = r+dr
		cc = c+dc
		if 0<=rr<R and 0<=cc<C and grid[rr][cc]!='#':
			q.append(((rr,cc),steps+1))
ans = 0
for v in S.values():
	if v%2 == 0:
		ans +=1
print(ans)
