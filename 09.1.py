import I
x = len(I.input[0])
t = 0
for i in range(len(I.input)):
	for j in range(x):
		h = int(I.input[i][j])
		if h < min(
			int([(9, *r, 9) for r in ([9] * x, *I.input, [9] * x)]
				[i + d // 3][j + d % 3])
			for d in (1, 3, 5, 7)):
			t += h + 1
print(t)