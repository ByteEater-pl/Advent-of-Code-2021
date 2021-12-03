import I
h = 0
d = 0
aim = 0
for l in I.input:
	c, _, n = l.partition(' ')
	n = int(n)
	try: aim += {'down': n, 'up': -n}[c]
	except:
		h += n
		d += n * aim
print(h * aim, h * d)