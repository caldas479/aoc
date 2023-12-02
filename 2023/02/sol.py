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
    r = b = g = 0
    for play in sets:
        moves = play.strip().split(',')
        
        for move in moves:
            move = move.strip().split(' ')
            n = int(move[0])
            color = move[1]
            if color == 'red':
                r = max(r,n)
            elif color == 'blue':
                b = max(b,n)
            else:
                g = max(g,n)
        
    ans += r*g*b

print(ans)
