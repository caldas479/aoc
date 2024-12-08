import sys
from collections import defaultdict

D = open(sys.argv[1]).read().strip().split('\n')

antennas = defaultdict(list)
X = len(D)
Y = len(D[0])

def is_valid(x, y):
    return 0 <= x < X and 0 <= y < Y

for x in range(X):
    for y in range(Y):
        if D[x][y] != '.':
            antennas[D[x][y]].append((x, y))

unique = set()
for freq, positions in antennas.items():
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            po = positions[i]
            pt = positions[j]
            xo, yo = po
            xt, yt = pt
            dx, dy = xt - xo, yt - yo

            p1 = (xo - dx, yo - dy)
            while is_valid(p1[0], p1[1]):
                unique.add(p1)
                p1 = (p1[0] - dx, p1[1] - dy)

            p2 = (xt + dx, yt + dy)
            while is_valid(p2[0], p2[1]):
                unique.add(p2)
                p2 = (p2[0] + dx, p2[1] + dy)

    unique.update(positions)


print(len(unique))
