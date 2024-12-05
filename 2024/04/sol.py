import sys

D = open(sys.argv[1]).read().strip().split('\n')

word = "XMAS"

X = len(D)
Y = len(D[0])

def search_direction(x,y,dx,dy):
	for i in range(len(word)):
		xx,yy = x + i*dx, y + i*dy
		if xx < 0 or yy < 0 or xx >= X or yy >= Y or D[xx][yy] != word[i]:
			return False
	return True

def search_x(x,y):
	ul = (x-1,y-1)
	ur = (x-1,y+1)
	dl = (x+1,y-1)
	dr = (x+1,y+1)
	corners = [ul,ur,dl,dr]
	for c in corners:
		cx, cy = c
		if cx < 0 or cy < 0 or cx >= X or cy >= Y:
			return False
	down_diagonal = D[ul[0]][ul[1]] + D[dr[0]][dr[1]]
	up_diagonal = D[ur[0]][ur[1]] + D[dl[0]][dl[1]]
	if down_diagonal == up_diagonal and down_diagonal in ["SM","MS"]:
		return True
	
	up = D[ul[0]][ul[1]] + D[ur[0]][ur[1]]
	down = D[dl[0]][dl[1]] + D[dr[0]][dr[1]]
	if up == "MM" and down == "SS" or up == "SS" and down == "MM":
		return True
	
	left = D[ul[0]][ul[1]] + D[dl[0]][dl[1]]
	rigth = D[ur[0]][ur[1]] + D[dr[0]][dr[1]]
	if left == "MM" and rigth == "SS" or left == "SS" and rigth == "MM":
		return True

dirs = [(1,0),
	(0,1),
	(-1,0),
	(0,-1),
	(1,-1),
	(-1,1),
	(1,1),
	(-1,-1)]

p1 = p2 = 0
for x in range(X):
	for y in range(Y):
		for dx,dy in dirs:
			if search_direction(x,y,dx,dy):
				p1+=1
		if D[x][y] == "A":
			if search_x(x,y):
				p2+=1
print(p1)
print(p2)
