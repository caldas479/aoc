"""
CREDITS TO HYPERNEUTRINO
"""

import sys

data = open(sys.argv[1]).read().strip().split('\n')

class Module:
	def __init__(self,name,type,outs):
		self.name = name
		self.type = type
		self.outs = outs

		if self.type == "&":
			self.mem={}
		else:
			self.mem="off"

	def __repr__(self):
		return "type: "+self.type+" -> "+ ",".join(self.outs) + "; MEM="+str(self.mem)
M = {}
b_out = []
for row in data:
	mod, outs = row.strip().split(' -> ')
	outs = outs.split(', ')
	if mod == "broadcaster":
		b_out = outs
	else:
		type = mod[0]
		name = mod[1:]
		M[name] = Module(name,type,outs)

for name, mod in M.items():
	for out in mod.outs:
		if out in M and M[out].type=="&":
			M[out].mem[name]= "low"


low = hi = 0
for _ in range(1000):
	low+=1
	q = [("broadcaster",out,"low") for out in b_out]

	while q:
		inp, out, p = q.pop(0)
		if p == "low":
			low+=1
		else:
			hi+=1


		if out not in M:
			continue

		mod = M[out]
		if mod.type == "%":
			if p=="low":
				mod.mem="on" if mod.mem=="off" else "off"
				pulse="hi" if mod.mem=="on" else "low"
				for o in mod.outs:
					q.append((mod.name,o,pulse))
		else:
			mod.mem[inp] = p
			pulse ="low" if all(x=="hi" for x in mod.mem.values()) else "hi"
			for o in mod.outs:
				q.append((mod.name,o,pulse))

print(low*hi)
