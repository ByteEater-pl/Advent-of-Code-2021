import I
*ps, = map(int, I.input[0].split(','))
print(
	sum(abs(p - sorted(ps)[len(ps) // 2]) for p in ps),
	min( # linear search; could be optimized, as the minima are 1 or 2 consecutive
		sum((2 * abs(p - x) + 1) ** 2 - 1 for p in ps)
		for x in range(min(ps), max(ps) + 1)
		) // 8)