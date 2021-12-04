import I

def det(xs, s):
	return '1' if (-1) ** s * (len(xs) - 2 * xs.count('1')) > -s else '0'

def toInt(l):
	return int(''.join(l), 2)

n = toInt(det(c, 1) for c in zip(*I.input))

def process(s):
	def go(xs, s):
		if len(xs) > 1:
			h = det([x[0] for x in xs], s)
			return h, *go([x[1:] for x in xs if x[0] == h], s)
		return xs[0]
	return toInt(go(I.input, s))

print(n * (2 ** len(I.input[0]) - 1 - n), process(1) * process(0))