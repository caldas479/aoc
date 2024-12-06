import sys
from collections import defaultdict

def update_is_correct(u):
	for i in range(len(u)):
		for j in range(i,len(u)):
			if u[i] in precedence[u[j]]:
				return False
	return True

def order_update(u):
	for i in range(len(u)):
		for j in range(i,len(u)):
			if u[i] in precedence[u[j]]:
				u[i],u[j] = u[j],u[i]
				return u

D = open(sys.argv[1]).read().strip().split('\n\n')

P = D[0].split('\n')
U = D[1].split('\n')

precedence = defaultdict(set)

for p in P:
	x,y = p.split('|')
	precedence[x].add(y)

p1 = p2 = 0
for u in U:
	u = u.split(',')
	if update_is_correct(u):
		p1 += int(u[len(u)//2])
	else:
		u = order_update(u)
		while not update_is_correct(u):
			u = order_update(u)
		p2 += int(u[len(u)//2])

print(p1)
print(p2)

