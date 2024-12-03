import sys

wfs, ratings = open(sys.argv[1]).read().strip().split('\n\n')

WF = {}

for wf in wfs.split('\n'):
	w, r = wf.split('{')
	WF[w] = [rule for rule in r[:-1].split(',')]

def accept(x,m,a,s):
	w = 'in'
	while True:
		rules = WF[w]
		for r in rules:
			if ':' in r:
				cond, state = r.split(':')
				if cond[1] == '<':
					part, val = cond.split('<')
					val = int(val)
					if ((part == 'x' and x < val) or
						(part == 'm' and m < val) or
						(part == 'a' and a < val) or
						(part == 's' and s < val)):
							if state == 'A':
								return True
							if state == 'R':
								return False
							w = state
							break
				else:
					part, val = cond.split('>')
					val = int(val)
					if ((part == 'x' and x > val) or
						(part == 'm' and m > val) or
						(part == 'a' and a > val) or
						(part == 's' and s > val)):
							if state == 'A':
								return True
							if state == 'R':
								return False
							w = state
							break
			else:
				if r == 'A':
					return True
				if r == 'R':
					return False
				w = r
ans = 0
for rates in ratings.split('\n'):
	rates = rates[1:-1].split(',')
	for r in rates:
		p, val = r.split('=')
		if p == 'x':
			x = int(val)
		elif p == 'm':
			m = int(val)
		elif p == 'a':
			a = int(val)
		elif p == 's':
			s = int(val)
	if accept(x,m,a,s):
		ans += x+m+a+s
print(ans)
