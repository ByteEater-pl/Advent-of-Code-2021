import I
coords = []
x_max = 0
y_max = 0
for l in I.input:
	*t, = map(int, l.replace(' -> ', ',').split(','))
	coords += [t]
	x_max = max(x_max, t[0], t[2])
	y_max = max(y_max, t[1], t[3])
f_diag, f_no_diag = (
	[[0] * (y_max + 1) for _ in range(x_max + 1)] for _ in range(2))
c_diag = 0
c_no_diag = 0
for x, y, x2, y2 in coords:
	no_diag = x == x2 or y == y2
	while True:
		def count(f):
			f[x][y] += 1
			return f[x][y] == 2
		c_diag += count(f_diag)
		if no_diag:
			c_no_diag += count(f_no_diag)
		if x == x2 and y == y2: break
		x += (x < x2) - (x > x2)
		y += (y < y2) - (y > y2)
print(c_no_diag, c_diag)