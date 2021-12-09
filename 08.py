import I, re

print(sum(
	len(re.findall(r' (\w{2,4}|\w{7})\b(?!.*\|)', l))
	for l in I.input))

t = 0
for l in I.input:
	ds = re.findall('\w+', l)
	n = 0
	for d in ds[10:]:
		n = 10 * n + (
				245, 94, 203, 241, 166, 231, 247, 150, 287, 271
			).index(
				sum([x * y for x, y in
						[(sum(s in m for m in ds[:10] if len(m) > b) for b in (0, 4))]
					][0] for s in d))
	t += n
print(t)