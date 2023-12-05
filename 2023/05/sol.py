import sys

data = open(sys.argv[1]).read().strip()
lines = [l for l in data.split('\n') if l!='']
seeds = lines[0].split(':')[1]
seeds = [int(n) for n in seeds.split()]
translate =  {}
for line in lines[1:]:       
    if line[0].isdigit():
        nums = [int(n) for n in line.split()]
        for i,s in enumerate(seeds):
            if nums[1] <= s < nums[1] + nums[2]:
                translate[s] = nums[0] + (seeds[i] - nums[1])
    else:
        for i,s in enumerate(seeds):
            if s in translate:
                seeds[i] = translate[s]
        translate = {}

print(min(seeds))