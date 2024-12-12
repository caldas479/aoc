import sys

D = open(sys.argv[1]).read().strip().split('\n')

X, Y = len(D), len(D[0])

SEEN = set()

def fence_price(pos, type, p1):

    area = 0
    peri = 0
    sides = 0
    q = [pos]
    while q:
        pos = q.pop(0)
        if pos in SEEN:
            continue
        SEEN.add(pos)

        x,y = pos
        if D[x][y] == type:
            area += 1
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        for dx, dy in dirs:
            xx, yy = x + dx, y + dy

            if xx < 0 or xx >= X or yy < 0 or yy >= Y or D[xx][yy] != type:
                peri += 1

            else:
                q.append((xx,yy))

    return area*peri if p1 else area*sides

p1 = 0
for x in range(X):
    for y in range(Y):
        if (x,y) not in SEEN:
            p1 += fence_price((x,y),D[x][y], p1 = True)

print(p1)


