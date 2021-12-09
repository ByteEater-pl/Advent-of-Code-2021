import I

input = [l.split() for l in I.input]

print(sum(len(x) in (2, 3, 4, 7) for r in input for x in r[11:]))

t = 0
for r in input:
	n = 0
	for d in r[11:]:
		n = 10 * n + (
				245, 94, 203, 241, 166, 231, 247, 150, 287, 271
			).index(
				sum([x * y for x, y in
						[(sum(s in m for m in r[:10] if len(m) > b) for b in (0, 4))]
					][0] for s in d))
	t += n
print(t)