import sys

data = open(sys.argv[1]).read().strip()
lines = data.split('\n')

seeds = lines[0].split(':')[1]
seeds = [int(n) for n in seeds.split()]

lines = lines[1:]
translate =  {}
for line in lines:
    if not len(line):
        for i,s in enumerate(seeds):
            if s in translate:
                seeds[i] = translate[s]
        translate = {}
         
    elif line[0].isdigit():
        nums = [int(n) for n in line.split()]
        i = 0
        for i,s in enumerate(seeds):
            if nums[1] <= s < nums[1] + nums[2]:
                translate[s] = nums[0] + (seeds[i] - nums[1])

for i,s in enumerate(seeds):
    if s in translate:
        seeds[i] = translate[s]

ans = 100000000000
for s in seeds:
    ans = min(ans,s)
print(ans)