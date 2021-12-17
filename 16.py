import I, math
m = ''.join(format(int(d, 16), '0>4b') for d in I.input[0])
a = 0
S = [[0, 0, []], [False, 1, [2]]]
while S[1:]:
	a += int(m[:3], 2)
	S[-1][1] -= not S[-1][0]
	t = int(m[3:6], 2)
	if t == 4:
		l = 5 * m[6::5].index('0') + 11
		S[-1][2] += int(''.join(m[i] for i in range(6, l) if i % 5 - 1), 2),
	else:
		c = not int(m[6])
		l = 22 if c else 18
		S += [c, int(m[7:l], 2) + c * 22, [t]],
	for e in S: e[1] -= e[0] * l
	while S[1:] and S[-1][1] == 0:
		f, *r = S.pop()[2]
		S[-1][2] += (sum, math.prod, min, max, 0, int.__gt__, int.__lt__, int.__eq__
			)[f](*([r] if f < 4 else r)),
	m = m[l:]
print(a, *S[0][2])