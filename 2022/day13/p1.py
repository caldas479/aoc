import sys

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


sum = 0

for i, pair in enumerate(data.split('\n\n')):
	l, r = pair.split('\n')
	l = eval(l)
	r = eval(r)
	if compare(l,r) == 1:
		sum += 1+i
	
print(sum)