import I
xs, ys = zip(*sorted((l[:2], l[6]) for l in I.input[2:]))
s = int(len(xs) ** .5)
r = range(s)
M = {x[0]: i for x, i in zip(xs[::s], r)}
A = [[0] * s for _ in r]
for u, v in zip(I.input[0], I.input[0][1:]):
	A[M[u]][M[v]] += 1
for n in 10, 30:
	for _ in range(n):
		B = [[0] * s for _ in r]
		for i in r:
			for j in r:
				k = M[ys[s * i + j]]
				B[i][k] += A[i][j]
				B[k][j] += A[i][j]
		A = B
	T = [sum(A[i]) + (i == M[I.input[0][-1]]) for i in r]
	print(max(T) - min(T))