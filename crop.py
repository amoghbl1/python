f = open("marks","r")
flag = 0
for line in f:
	if flag == 1:
		flag = 0
		print line
	if "Name" in line:
		print line
	if "SGPA" in line:
		flag = 1
