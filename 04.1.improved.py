def loop():
	import I
	ns = [*map(int, I.input[0].split(','))]
	D = {n: set() for n in ns}
	sums = []
	for i in range(2, len(I.input), 6):
		b = I.input[i:][:5]
		sums += [0]
		for r in range(5):
			v = b[r].split()
			for c in range(5):
				D[int(v[c])].add((i // 6, r, c))
				sums[-1] += int(v[c])
	unmarked = [[[5] * 5 for _ in range(2)] for _ in sums]
	for n in ns:
		for k, r, c in D[n]:
			unmarked[k][0][r] -= 1
			unmarked[k][1][c] -= 1
			sums[k] -= n
			if unmarked[k][0][r] * unmarked[k][1][c] == 0:
				print(sums[k] * n)
				return
loop()