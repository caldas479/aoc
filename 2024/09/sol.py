import sys

D = open(sys.argv[1]).read().strip().split('\n')[0]

file = True
blocks = []
id = 0
for x in D:
	x = int(x)
	if file:
		blocks += [str(id)]*x
		id += 1
		file = False
	else:
		blocks += ['.']*x
		file = True
		
blocks2 = blocks.copy()

# First free block
l = 0
while (blocks[l] != '.'):
	l += 1

spans = [] # (start index, span size)

# Find first empty span
ll = l
span = 0
while(blocks[ll] == '.'):
	span += 1
	ll += 1

# Find empty space spans
spans += [(l,span)]
while(ll < len(blocks)):
		span = 0
		start = ll
		while(blocks[ll] == '.'):
			span += 1
			ll += 1
		if span == 0:
			ll += 1
		else:
			spans += [(start,span)]

# Find fist block to move
r = len(blocks)-1
while (blocks[r] == '.'):
	r -= 1

# Find blocks set
blocks_set = [] # (last,bset,id)
bset = 0
rr = r
while(rr >= 0):
	while (blocks[rr] == '.'):
		rr -=1

	bset = 0
	last = rr
	id = blocks[last]
	while (blocks[rr] == id):
		rr -= 1
		bset += 1
	if bset == 0:
		rr -= 1
	else:
		blocks_set += [(last,bset,id)]

# part 1
while r > l:
	blocks[l],blocks[r] = blocks[r],blocks[l]
	while (blocks[l] != '.'):
		l += 1
	while (blocks[r] == '.'):
		r -= 1

checksum = sum(i * int(b) for i, b in enumerate(blocks) if b != '.')
print(checksum)

# part 2
for block_set in blocks_set:
	j, bset, id = block_set
	for si,s in enumerate(spans):
		i, span = s
		# there is space to move the blocks
		if bset <= span:
			while (bset > 0):
				blocks2[i], blocks2[j] = blocks2[j],blocks2[i]
				i += 1
				j -= 1
				bset -= 1
				span -= 1
			spans[si] = (i,span)
			break
	
checksum = sum(i * int(b) for i, b in enumerate(blocks2) if b != '.')
print(checksum)





