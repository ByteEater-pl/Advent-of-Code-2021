import I
F = [0] * 9
for n in I.input[0].split(','):
	F[int(n)] += 1
for i in range(256):
	F = *F[1:7], F[7] + F[0], F[8], F[0]
	if i in (79, 255): print(sum(F))