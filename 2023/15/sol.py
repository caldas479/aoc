import sys

data = open(sys.argv[1]).read().strip().split('\n')
p1 = p2 = 0
def hash(s):
    curr = 0
    for ch in s:
        curr += ord(ch)
        curr *= 17
        curr %= 256
    return curr
boxes = [[] for _ in range(256)]
focal = {}
for step in data[0].split(','):
    p1 += hash(step)
    if "-" in step:
        label = step[:-1]
        i = hash(label)
        if label in boxes[i]:
            boxes[i].remove(label)
    else:
        label, l = step.split("=")
        l = int(l)
        i = hash(label)
        if label not in boxes[i]:
            boxes[i].append(label)
        focal[label]  = l
    
for ib, box in enumerate(boxes,1):
    for il, label in enumerate(box,1):
        p2 += ib*il*focal[label]
print(p1,p2)