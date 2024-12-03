from collections import Counter
import sys

data = open(sys.argv[1]).read().strip().split('\n')

def is_valid(springs,nums):
    springs = springs.split('.')
    groups = [len(x) for x in springs if len(x) > 0]
    return groups == nums

def f(springs,nums,i):
    if(i==len(springs)):
        return 1 if is_valid(springs,nums) else 0
    elif(springs[i]=='?'):  
        return f(springs[:i]+'#'+springs[i+1:],nums,i+1) + f(springs[:i]+'.'+springs[i+1:],nums,i+1)
    else:
        return f(springs,nums,i+1)
ans = 0
for row in data:
    springs, nums = row.split()
    nums = [int(n) for n in nums.split(',')]
    #ans += f(springs,nums,0)
    