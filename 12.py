import I
def search(s, visited, re):
	re |= s in visited
	return 1 if s == 'end' else sum(
		search(n, visited | set(filter(str.islower, [s])), re)
		for n in
			{(e - {s}).pop() for l in I.input for e in [set(l.split('-'))] if s in e}
			- (visited if re else {'start'}))
print([search('start', set(), re) for re in (True, False)])