sgpa = open("sgpa","r")
for i in sgpa:
	if "<div >" in i:
		print i.strip('<div ><font style="background-color:#3399FF">Name&nbsp;:&nbsp;').strip().strip("</font></div>")
	if "<strong>" in i:
		print i.strip().strip("<strong>").strip("</strong></td>") 
