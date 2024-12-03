input_file = 'A.txt'
D = []

with open(input_file, 'r') as file:
    D = file.readlines()

X = []
Y = []

X_COUNT = {}
Y_COUNT = {}

for line in D:
	x,y = line.split()
	X.append(int(x))
	Y.append(int(y))
	if x in X_COUNT:
		X_COUNT[x]+=1
	else:
		X_COUNT[x]=1
	if y in Y_COUNT:
		Y_COUNT[y]+=1
	else:
		Y_COUNT[y]=1
X.sort()
Y.sort()

ans=0
p2=0
for i in range(len(X)):
	ans += abs(X[i]-Y[i])


for x in X_COUNT:
	if x in Y_COUNT:
		p2+= int(x)*Y_COUNT[x]


print(ans)
print(p2)
