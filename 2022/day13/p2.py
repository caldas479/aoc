import sys
from functools import cmp_to_key
infile = sys.argv[1] if len(sys.argv) > 1 else 'in.txt'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

def compare(l,r):
	if isinstance(l,int) and isinstance(r,int):
		if l < r:
			return 1
		elif l == r:
			return 0
		else:
			return -1
	elif isinstance(l,list) and isinstance(r,list):
		i = 0
		while i < len(l) and i < len(r):
			c = compare(l[i],r[i])
			if c != 0:
				return c
			i+=1

		if i == len(l) and i < len(r):
			return 1
		elif i < len(l) and i == len(r):
			return -1
		else:
			return 0

	elif isinstance(l,list) and isinstance(r,int):
		return compare(l,[r])

	elif isinstance(l,int) and isinstance(r,list):
		return compare([l],r)

res = 1
packs = [[[2]],[[6]]]

for i, pair in enumerate(data.split('\n\n')):
	l, r = pair.split('\n')
	l = eval(l)
	r = eval(r)
	packs.append(l)
	packs.append(r)

packs = sorted(packs, key=cmp_to_key(lambda l,r: compare(l,r)), reverse = True)


for i,p in enumerate(packs):
    if p==[[2]] or p==[[6]]:
        res *= i+1
print(res)
		
	

