import re
textTemp = ""
# Open/Create a file to append data
textFile = open('data3.txt', 'a+')

with open('tweetsdata.csv','Ur') as file:
    for line in file:
	textTemp = ""
	extractedData = re.findall(r'[#@][^\s#@]+', line) 
	extractedData += re.findall("(?P<url>https?://[^\s]+)",line)
	print "extracting"
	for data in extractedData:
	    textTemp += " "+data
        textFile.write(textTemp)

#close file
textFile.close()
