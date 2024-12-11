import sys
from functools import cache

D = open(sys.argv[1]).read().strip().split('\n')
L = D[0].split()

@cache
def optimize(n, blinks):
    if blinks == 0:
        return 1
    if n == 0:
        return optimize(1, blinks - 1)

    s = str(n)
    if len(s) % 2 == 0:
        return (
            optimize(int(s[:len(s) // 2]), blinks - 1)
            + optimize(int(s[len(s) // 2:]), blinks - 1)
        )
    return optimize(n * 2024, blinks - 1)

stones = [int(x) for x in L]
print(sum(optimize(stone, 75) for stone in stones))
