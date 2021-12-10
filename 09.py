import I, math
w = len(I.input[0])
M = [[9, *r, 9] for r in ([9] * w, *I.input, [9] * w)]
a = 0
lows = []
ds = (1, 3, 5, 7)
for i in range(len(I.input)):
	for j in range(w):
		h = int(I.input[i][j])
		if h < min(
			int(M[i + d // 3][j + d % 3])
				for d in ds):
			a += h + 1
			lows += [[(i + 1, j + 1)]]
bs = ()
for bd in lows:
	s = 0
	for x, y in bd:
		for d in (4, *ds):
			i = x - 1 + d // 3
			j = y - 1 + d % 3
			if int(M[i][j]) < 9:
				M[i][j] = 9
				bd += [(i, j)]
				s += 1
	p = next((i for i, x in enumerate(bs) if x < s), 3)
	bs = (*bs[:p], s, *bs[p:])[:3]
print(a, math.prod(bs))