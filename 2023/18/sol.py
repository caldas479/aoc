import sys

data = open(sys.argv[1]).read().strip().split('\n')

dir = {"D": (1,0),"U":(-1,0),"L":(0,-1),"R":(0,1)}

seen = [(0,0)]
boundarie = 0
for row in data:
    d,n,c = row.split()
    n = int(n)
    boundarie +=n
    x,y = seen[-1]
    dx,dy = dir[d]
    xx = x + dx*n
    yy = y + dy*n
    seen.append((xx,yy))

"""
https://en.wikipedia.org/wiki/Shoelace_formula
"""
A = abs(sum(seen[i][0] * (seen[i-1][1] - seen[(i+1)%len(seen)][1]) for i in range(len(seen))))//2
interior = A - boundarie//2+1
print(interior+boundarie)