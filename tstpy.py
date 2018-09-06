array = ([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

r = 100
for i in range(0, 3):
	for j in range (0, 3):
		array[i][j] = r
		j = j + 1
		r = r + 1
	i = i + 1

print(array)