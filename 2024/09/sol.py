import sys

D = open(sys.argv[1]).read().strip().split('\n')[0]

file = True
blocks = []
id = 0
for x in D:
	x = int(x)
	if file:
		blocks += [id]*x
		id += 1
		file = False
	else:
		blocks += ['.']*x
		file = True
            
l = 0
r = len(blocks)-1

while (blocks[l] != '.'):
	l += 1
while (blocks[r] == '.'):
	r -= 1

while r > l:
	blocks[l],blocks[r] = blocks[r],blocks[l]
	while (blocks[l] != '.'):
		l += 1
	while (blocks[r] == '.'):
		r -= 1

checksum = sum(i * int(b) for i, b in enumerate(blocks) if b != '.')
print(checksum)


