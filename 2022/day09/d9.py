import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'in.txt'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

head = (0,0)
tail = [(0,0) for _ in range(9)]

p1 = set()
p2 = set()

def update(head,tail):
    dr = abs(head[0] -tail[0])
    dc = abs(head[1] - tail[1])
    if dr <= 1 and dc <= 1:
            pass
    elif dr >= 2:
        tail = (head[0] - 1 if tail[0] < head[0] else head[0] + 1, head[1])
    elif dc >= 2:
        tail = (head[0],head[1]-1 if tail[1] < head[1] else head[1] + 1)
    elif dr>=2 and dc>=2:
        tail = (head[0]-1 if tail[0]<head[0] else head[0]+1, head[1]-1 if tail[1]<head[1] else head[1]+1)    
    return tail

for line in lines:
    dir, n = line.split()
    if dir == "R":
        move = (0,1)
    elif dir == "L":
        move = (0,-1)
    elif dir == "U":
        move = (-1,0)
    else:
        move = (1,0)
    for _ in range(int(n)):
        p1.add(tail[0])
        p2.add(tail[8])
        head = (head[0] + move[0], head[1] + move[1])
        tail[0] = update(head,tail[0])
        for i in range(1,9):
            tail[i] = update(tail[i-1],tail[i])
        p1.add(tail[0])
        p2.add(tail[8])
print(len(p1))
print(len(p2))