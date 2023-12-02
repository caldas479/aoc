import sys
import numpy as np

from collections import defaultdict

infile = sys.argv[1] if len(sys.argv) > 1 else 'in.txt'
data = open(infile).read().strip().split()

N = len(data)
M = len(data[0])
grid = np.array([list(map(int,list(line))) for line in data])
DIR = [(1,0),(-1,0),(0,-1),(0,1)]
ans = 0
for r in range(N):
    for c in range(M):
        h = grid[r,c]
        score = 1
        for x,y in DIR:
            dr = r+x
            dc = c+y
            dist = 0
            
            while(0 <= dr < N and 0 <= dc < N) and grid[dr,dc] < h:
                dist += 1
                dr += x
                dc += y

                if(0 <= dr < N and 0 <= dc < N) and grid[dr,dc] >= h :
                    dist += 1
            score *= dist
        ans = max(score,ans)
print(ans)  

