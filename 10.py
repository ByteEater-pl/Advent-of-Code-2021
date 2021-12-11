import I
a = 0
ts = []
d = {')': 3, ']': 57, '}': 1197, '>': 25137}
for l in I.input:
	S = ''
	for c in l:
		try:
			if S[:1] == str([0, *d].index(c)): S = S[1:]
			else:
				a += d[c]
				break
		except: S = str('_([{<'.index(c)) + S
	else: ts += [int(S, 5)]
print(a, sorted(ts)[len(ts) // 2])