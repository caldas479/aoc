import sys
import re

D = open(sys.argv[1]).read().strip().split('\n')

ans = 0
mul_enabled = True

pattern_mul = r"mul\((\d{1,3}),(\d{1,3})\)|(do|don't)\(\)"

for expr in D:
    for match in re.finditer(pattern_mul, expr):

        instruction = match.group()

        if instruction == "do()":
            mul_enabled = True
        elif instruction == "don't()":
            mul_enabled = False
        elif mul_enabled and instruction.startswith("mul"):
            x, y = map(int, re.match(r"mul\((\d{1,3}),(\d{1,3})\)", instruction).groups())
            ans += x * y

print(ans)
