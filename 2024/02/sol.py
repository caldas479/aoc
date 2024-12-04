import sys

def is_safe(levels):
    prev = int(levels[0])
    first = True
    inc = dec = False
    for l in levels[1:]:
        l = int(l)
        if abs(l - prev) > 3 or l == prev or (l > prev and dec) or (l < prev and inc):
            return False
        if l < prev and first:
            dec = True
            first = False
        elif l > prev and first:
            inc = True
            first = False
        prev = l
    return True

D = open(sys.argv[1]).read().strip().split('\n')
ans = 0

for report in D:
    levels = list(map(int, report.split()))
    # Check if the report is safe without modifications
    if is_safe(levels):
        ans += 1
    else:
        # Check if removing a single level makes the report safe
        for i in range(len(levels)):
            modified_levels = levels[:i] + levels[i+1:]
            if is_safe(modified_levels):
                ans += 1
                break

print(ans)
