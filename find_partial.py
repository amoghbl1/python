import os,sys
path = sys.argv[1]
find = sys.argv[2]
walk = os.walk(path)
for i in walk:
	for j in i:
		for k in j:
			if find in k:
				print "found file at "+os.path.abspath(i[0])
