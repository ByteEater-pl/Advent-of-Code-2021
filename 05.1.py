import I
coords = []
x_max = 0
y_max = 0
for l in I.input:
	x1, y1, x2, y2 = map(int, l.replace(' -> ', ',').split(','))
	if x1 == x2 or y1 == y2:
		coords += [sorted((x1, x2)) + sorted((y1, y2))]
		x_max = max(x_max, x1, x2)
		y_max = max(y_max, y1, y2)
field = [[0] * (y_max + 1) for _ in range(x_max + 1)]
c = 0
for x1, x2, y1, y2 in coords:
	for x in range(x1, x2 + 1):
		for y in range(y1, y2 + 1):
			field[x][y] += 1
			if field[x][y] == 2:
				c += 1
print(c)