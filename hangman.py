import random,os

def read1QA():
	qa=open("QA.txt","r")
        QL=[]
        AL=[]
        QAL=[]
	Q="temp"
	while Q != "":
		Q=qa.readline()
	        A=qa.readline()
	        QL.append(Q)
        	AL.append(A)
	        QAL.append(QL)
		QAL.append(AL)
        return QAL

def check(g,a,ua):
	for i in g:
		index=0
		while index<len(a):
			previndex=index
			index=a.find(i,index)
			if index == -1:
				break
 		  	Lua=list(ua)
			Lua.pop(index)
			Lua.insert(index,i)
			ua="".join(Lua)
			if previndex == index:
				index = index+1

        return ua



def main():
        QAL=read1QA()
	QL=QAL[0]
	AL=QAL[1]
        CAC=0
	QC=len(QL)-1

        for j in range(1,len(QL)):
		gc=5
        	usrans=""
        	qaindex=random.randint(0,(len(QL)-2))
		print qaindex
		for i in range(1,len(AL[qaindex])):
	   		usrans=usrans+"_"

		for i in range(0,gc):
			os.system("clear")
                	print " "
			print QL[qaindex]
			print usrans
        		print "Guesses left ",gc
	        	guess=raw_input("Enter Guess")
		        usrans=check(guess,AL[qaindex],usrans)
        		gc=gc-1
		        if (usrans+"\n") == AL[qaindex]:
				print "Correct Answer!!!"
 				CAC=CAC+1
				break
       
		print "Answer was: ", AL[qaindex]
		QL.pop(qaindex)
		AL.pop(qaindex)
		raw_input("Press Enter for next Question")
		os.system("clear")

	print "Game Over!!!", CAC, "Answered Correct Out Of", QC

main()
