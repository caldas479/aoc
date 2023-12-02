input_file = 'input.txt'
lines = []

with open(input_file, 'r') as file:
    lines = file.readlines()

ans = 0

elf_bag = {'red': 12, 'green': 13, 'blue': 14}

for id, game in enumerate(lines):
    game = game.strip().split(':')
    sets = game[1].split(';')
    valid = True
    for play in sets:
        moves = play.strip().split(',')
        r = b = g = 0
        for move in moves:
            move = move.strip().split(' ')
            n = int(move[0])
            color = move[1]
            if elf_bag[color] < n:
                valid = False
    if valid:
        ans += id + 1

print(ans)
