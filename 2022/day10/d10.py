import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'in.txt'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

X = 1
N = 0
reg = [["." for _ in range(40)] for _ in range(6)]

def draw(l,c):
    if X - 1 == c or X == c or X+1 == c:
        reg[l][c] = "#"

l = 0
c = 0
for line in lines:
    words = line.split()
    instruct = words[0]
    v = 0 if instruct == "noop" else int(words[1])
    if instruct == "addx":
        N += 1
        draw(l,c)
        c += 1
        if c == 40:
            c = 0
            l += 1
    N += 1
    draw(l,c)
    c += 1
    if c == 40:
        c = 0
        l += 1
    X += v
    
for i in range(len(reg)):
    print(''.join(reg[i]))
        
        