import sys

data = open(sys.argv[1]).read().strip()
times,distances = data.split('\n')
times = [n for n in times.split()[1:]]
distances = [n for n in distances.split()[1:]]
time = int(''.join(times))
distance = int(''.join(distances))
ans = 1
won = 0
for j in range(1,time):
    if (j * (time-j)) > distance:
        won += 1
ans *= won

print(ans)