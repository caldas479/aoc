import sys
from sympy import symbols, solve
data = open(sys.argv[1]).read().strip().split('\n')
least = 200000000000000
most = 400000000000000
hailstones = []
for l in data:
	pos,vel = l.split(' @ ')
	pos = [int(n) for n in pos.split(', ')]
	vel = [int(n) for n in vel.split(', ')]
	hailstones.append((pos,vel))

ans = 0
for i, hs in enumerate(hailstones):
	for j in range(i+1,len(hailstones)):
		ipos, ivel = hs
		ix,iy,_ = ipos
		ivx,ivy,_= ivel

		jpos,jvel = hailstones[j]
		jx,jy,_ = jpos
		jvx,jvy,_= jvel
		
		px,py = symbols("px py")

		sols = solve([ivy*(px-ix) - ivx*(py-iy),jvy*(px-jx) - jvx*(py-jy)])
		if sols:
			x,y = sols[px], sols[py]
			if least<=x<=most and least<=y<=most:
				if (x-ix)*ivx >= 0 and (y-iy)*ivy>=0 and (x-jx)*jvx >= 0 and (y-jy)*jvy>=0:
					ans +=1
print(ans)
