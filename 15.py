import I, heapq
def do(M):
	n = len(M)
	r = range(n)
	D = [[i + j and 9 * n * n for j in r] for i in r]
	Q = [(0, 0, 0)]
	S = set()
	while Q:
		w, i, j = heapq.heappop(Q)
		S.add((i, j))
		for d in 1, 3, 5, 7:
			x = i - 1 + d // 3
			y = j - 1 + d % 3
			if ((x, y) in S) < ({x, y} < set(r)):
				#print(w,i,j,x,y,S,Q)
				a = w + M[x][y]
				if a < D[x][y]:
					D[x][y] = a
					heapq.heappush(Q, (a, x, y))
	print(D[-1][-1])
P = [[*map(int, l)] for l in I.input]
do(P)
def ext(A):
	return [
		[(d + s - 1) % 9 + 1 for d in r]
		for s in range(5) for r in A]
do(ext([*zip(*ext(P))]))