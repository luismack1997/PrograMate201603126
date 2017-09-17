PathDict={(1,0):1}
for i in range(21):
	PathDict[(i,0)] = 1
	PathDict[(0,i)] = 1
for i in range(1,21):
	for j in range(1,21):
		PathDict[(i,j)]=PathDict[(i-1,j)]+PathDict[(i,j-1)]
print(PathDict[(20,20)])
