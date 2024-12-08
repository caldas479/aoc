import sys

from itertools import product

def concatenate(a, b):
    return int(f"{a}{b}")

def calculate_combinations(target, nums,part):
    num_operators = len(nums) - 1
    o = ['+', '*','||'] if part else ['+', '*']
    operator_combinations = product(o, repeat=num_operators)

    for operators in operator_combinations:
        total = nums[0]
        for i in range(len(operators)):
            if operators[i] == '+':
                total += nums[i + 1]
            elif operators[i] == '*':
                total *= nums[i + 1]
            elif operators[i] == '||' and part:
                total = concatenate(total, nums[i + 1])
        if total == target:
            return True
    return False


D = open(sys.argv[1]).read().strip().split('\n')

p1 = p2 = 0
for equation in D:
	target, nums = equation.split(':')
	target = int(target)
	nums = [int(x) for x in nums.split()]
	if calculate_combinations(target,nums,False):
		p1+=target
	if calculate_combinations(target,nums,True):
		p2+=target

print(p1)
print(p2)