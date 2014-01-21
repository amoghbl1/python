import mechanize
br = mechanize.Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
response = br.open("http://www.rvce.edu.in/results")
br.select_form(nr=0)
br['branch'] = ["21",]
br['sem'] = "1"
response = br.submit()
#print response.read()
for i in xrange(1,186):
	br.select_form(nr=0)
	fio = open("this","a")
	fio.write("\n")
	if (i<10):
		br['usn'] = "1RV13EC00"+str(i)
	elif(i<99):
		br['usn'] = "1RV13EC0"+str(i)
	else:
		br['usn'] = "1RV13EC"+str(i)
	response = br.submit()
	print response.read()
	#fio.write(response.read())
	#fio.close()
	#print "done "+str(i)
	#print response.read()
