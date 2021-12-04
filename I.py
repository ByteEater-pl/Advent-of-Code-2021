import sys, os
with open(
	os.path.basename(sys.modules['__main__'].__file__)
	.partition('.')[0]
	+ '.in') as f:
	input = [l[:-1] for l in f]