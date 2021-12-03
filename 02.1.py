import I, collections
totals = collections.Counter()
for l in I.input:
	t = l.partition(' ')
	totals[t[0]] += int(t[2])
print(totals['forward'] * (totals['down'] - totals['up']))