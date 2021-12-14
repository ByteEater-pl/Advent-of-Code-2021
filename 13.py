import I
e = I.input.index('')
ps = [[*map(int, l.split(','))] for l in I.input[:e]]
cs = [[int(l[13:]) for l in I.input[e:] if l[11:12] == a] for a in 'xy']
def fold(ts):
	for p in ps:
		for i in (0, 1):
			for t in ts[i]:
				p[i] = t - abs(t - p[i])
b = I.input[e + 1][11] > 'x'
fold((([cs[b].pop(0)], ()) * 2)[b:])
print(len(set(map(tuple, ps))))
fold(cs)
for j in range(cs[1][-1]):
	print(''.join(
		'#' if [i, j] in ps else '.'
		for i in range(cs[0][-1])))