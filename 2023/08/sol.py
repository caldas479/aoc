import sys
sys.setrecursionlimit(100000)
data = open(sys.argv[1]).read().strip().split('\n')
instructions = data[0]
nodes = {}
for line in data[2:]:
    n, lr = line.split('=')
    lr = lr.strip().split(',')
    nodes[n.strip()] = (lr[0][1:],lr[1].strip()[0:3])

def move(i, node):
    if i >= len(instructions):
        i = 0
    node = nodes[node][0] if instructions[i] == 'L' else nodes[node][1]
    if node == "ZZZ":
        return 1
    return 1 + move(i+1,node)

print(move(0,'AAA'))

