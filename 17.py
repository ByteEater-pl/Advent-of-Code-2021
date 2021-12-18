# incomplete
import I, re, math
xl, xh, yl, yh = map(int, re.findall('-?\d+', I.input[0]))
if xl < 0:
	xl, xh = (-xh, -xl) if xh < 0 else (0, max(-xl, xh))
y = 0
for v in range(xh + 1):
	q = v * v + v + .25
	a, b = (v + .5 - (q - 2 * e) ** .5 for e in (xl, xh))
	try:
		m = math.ceil(a)
		n = 2 * yh + 1 if b.imag else int(b)
		if m <= n:
			y = max(y, q / 2 if m <  < n else y, *(t * (v - .5) - t * t / 2 for t in (m, n)))
			print(v, a, b, y)
	except: pass
print(int(y))