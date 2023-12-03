input_file = 'input.txt'
lines = []

with open(input_file, 'r') as file:
    lines = file.readlines()

ans = 0

word2n = {"one":1, "two":2, "three":3, "four": 4, 
        "five":5, "six":6, "seven":7, "eight":8, "nine":9}

for line in lines:
    word = ""
    l = 0
    r = 1
    digits = []
    while(l < len(line)):
        c = line[l]
        if (c.isdigit()):
            digits += [int(c)]
        else:
            word = c
            while(r < len(line)):
                word += line[r]
                r += 1
                if (word in word2n):
                    digits += [word2n[word]]
        l += 1
        r = l + 1

    ans += digits[0]*10 + digits[-1]

print(ans)

