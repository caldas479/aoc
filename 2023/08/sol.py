import sys
from math import gcd

data = open(sys.argv[1]).read().strip().split('\n')
instructions = data[0]
net = {}
initials = []
for line in data[2:]:
    n, lr = line.split('=')
    lr = lr.strip().split(',')
    net[n.strip()] = (lr[0][1:],lr[1].strip()[0:3])
    if n[2] == 'A':
        initials += [n.strip()]

def lcm(arg):
    ans = 1
    for x in arg:
        ans = (x*ans)//gcd(x,ans)
    return ans

def move(nodes):
    steps = 0
    i = 0 
    z = [0 for i in range(len(nodes))]
    while (any(x == 0 for x in z)):
        steps += 1
        next_nodes = []
        if i >= len(instructions):
            i = 0 
        for ii, node in enumerate(nodes):
            next_node = net[node][0] if instructions[i] == 'L' else net[node][1]
            next_nodes += [next_node]
            if next_node[2] == 'Z':
                z[ii] = steps
        nodes = next_nodes
        i += 1
    return lcm(z)

print(move(initials))
                      
