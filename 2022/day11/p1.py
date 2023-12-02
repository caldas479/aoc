import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'in.txt'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

ITEMS = []
OP = []
TEST = []
TRUE = []
FALSE = []

for monkey in data.split('\n\n'):
    i, items, op, test, t, f = monkey.split('\n')
    ITEMS.append([int(x) for x in items.split(':')[1].split(',')])
    words = op.split()
    op = ''.join(words[-3:])
    OP.append(lambda old, op = op: eval(op))
    TEST.append(int(test.split()[-1]))
    TRUE.append(int(t.split()[-1]))
    FALSE.append(int(f.split()[-1]))

COUNT = [0 for _ in range(len(ITEMS))]

for _ in range(20):
    for i in range(len(ITEMS)):
        for item in ITEMS[i]:
            COUNT[i] += 1
            item = OP[i](item)
            item = (item // 3)
            if item % TEST[i] == 0:
                ITEMS[TRUE[i]].append(item)
            else:
                ITEMS[FALSE[i]].append(item)
        ITEMS[i] = []

print(sorted(COUNT))
print(sorted(COUNT)[-1] * sorted(COUNT)[-2])