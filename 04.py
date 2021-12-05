def loop():
	import I
	ns = I.input[0].split(',')
	D = {n: [] for n in ns}
	sums = []
	del I.input[:2]
	i = 0
	while len(I.input) > 5:
		b = I.input[:5]
		sums += [0]
		for r in range(5):
			t = b[r].split()
			for c in range(5):
				v = int(t[c])
				D[t[c]] += [(i, r, c, v)]
				sums[i] += v
		del I.input[:6]
		i += 1
	unmarked = [[[5] * 5 for _ in range(2)] for _ in sums]
	active = set()
	for n in ns:
		for j, r, c, v in D[n]:
			unmarked[j][0][r] -= 1
			unmarked[j][1][c] -= 1
			sums[j] -= v
			if unmarked[j][0][r] * unmarked[j][1][c] == 0:
				if active:
					active.discard(j)
					if active == set():
						print(sums[j] * v)
						return
				else:
					print(sums[j] * v)
					active = set(range(i))
loop()