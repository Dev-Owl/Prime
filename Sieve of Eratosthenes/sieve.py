"""
	Sieve of Eratosthenes from Christian Muehle with HTML output
	c.muehle18@googlemail.com
"""
import sys

def main():
	if( len( sys.argv[1:]) == 1) :
		
		tmp =0;
		startValue = 2
		endValue = int(sys.argv[1])+1
		
		if( endValue < startValue):
			endValue = startValue+1
		
		noPrime =  [False] * (endValue)
		print("Starting at "+ str( startValue)+ " and going to " + str(endValue))
		
		for x in range(startValue, endValue):
			#Working now
			if  not noPrime[x]:
				print( str(x))
				counter = x
				while x * counter <= endValue-1:
					noPrime[(x * counter)] = True
					counter +=1
		buildHTMLTemplate(startValue,endValue,noPrime)
	else:
		print("Please provide the end number to start the creation. For example 100000")
	

def buildHTMLTemplate(startValue, endValue, result):
	coloumLength=10;
	trTemplate="<tr>{0}</tr>"
	tdTemplateStart="<td id=\"{0}\">"
	tdTemplateEnd="{0}</td>"
	textResult= ""
	texttmp=""
	coloumCount = 0
	if( endValue > 100):
		coloumLength = 10
	elif ( endValue > 1000):
		coloumLength = 50
	elif ( endValue > 10000):
		coloumLength = 100
	
	print("Starting with template file");

	for x in range(startValue, endValue):
		if( coloumCount >= coloumLength):
			textResult += trTemplate.replace("{0}",texttmp)
			texttmp = ""
			coloumCount = 0
		
		if  not result[x]:
			texttmp += tdTemplateStart.replace("{0}","prime")
		else:
			texttmp += tdTemplateStart.replace("{0}","normal")
		
		texttmp += tdTemplateEnd.replace("{0}",str(x))
		coloumCount += 1
	textResult += trTemplate.replace("{0}",texttmp)
	
	file =open('primeTemplate.temp','r')
	target = open('result.html','w')
	target.write( file.read().replace("{0}",textResult))
	target.close()
	print("Done")
	
if __name__ == "__main__":
    main()