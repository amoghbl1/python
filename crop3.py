f = open("sgpa","r")
line = f.readline().strip("\n")
while line != "":
	if line == "\n":
		line = f.readline()
	mark = float(f.readline().strip("\n"))
	if mark > 8.5:
		print (str(mark)+" "+line.strip("\n"))
	line = f.readline()

