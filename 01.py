import I
depths = [*map(int, I.input)]
print([
	sum(x < y for x, y in zip(xs, xs[1:]))
	for xs in [
		depths,
		[*map(sum, zip(*(depths[n:] for n in range(3))))]]])