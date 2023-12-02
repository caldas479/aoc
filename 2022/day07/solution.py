import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv) > 1 else 'in.txt'
data = open(infile).read().strip()
lines = [line for line in data.split('\n')]

dirs_size = defaultdict(int)
path = []
for line in lines:
    tokens = line.strip().split()
    if tokens[1] == "cd":
        if tokens[2] == "..":
            path.pop()
        else:
            path.append(tokens[2])
    elif tokens[1] == "ls":
        continue
    else:
        try:
            size = int(tokens[0])
            for i in range(len(path)+1):
                dirs_size['/'.join(path[:i])] += size
        except:
            pass

used_space = dirs_size['']
unused_space = 70000000 - used_space
ans = 1e9
for k,v in dirs_size.items():
    if unused_space + v >= 30000000:
        ans = min(ans,v)

print(ans)


    