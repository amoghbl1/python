import os,sys
path = sys.argv[1]
find = sys.argv[2]
walk = os.walk(path)
for i in walk:
	for j in i:
		for k in j:
			try:
				open(k)
				if find in k.read():
					print "content in "+os.path.abspath(i[0])+"/"+k
			except Exception:
				pass
				#print ":|"
