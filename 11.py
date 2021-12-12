import I
G = [map(int, l) for l in I.input]
n = len(G)
d = range(n)
a = 0
s = 1
while True:
	G = [[e + 1 for e in v] for v in G]
	f = True
	while f:
		f = False
		for x in d:
			for y in d:
				if G[x][y] > 9:
					f = True
					for i in range(x - 1, x + 2):
						for j in range(y - 1, y + 2):
							if {i, j} < set(d):
								G[i][j] += G[i][j] > -1
					G[x][y] = -1
	c = 0
	for x in d:
		for y in d:
			if G[x][y] < 0:
				G[x][y] = 0
				c += 1
	a += c
	if s == 100: print(a)
	if c == n * n:
		print(s)
		break
	s += 1