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
       i=i.upper()
       index=a.find(i,previndex)
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
    c=0
    gc=5
    usrans=""
    qaindex=random.randint(0,(len(QL)-2))
    for i in range(1,len(AL[qaindex])):
      usrans=usrans+"_"
    
    usrans=check(" ",AL[qaindex],usrans)
    while gc>0:	 
      os.system("clear")
      print (" ")
      print (QL[qaindex])
      print (usrans)
      print ("Guesses left ",gc)
      guess=input("Enter Guess: ")
      prevuans=usrans
      usrans=check(guess,AL[qaindex],usrans)
      if usrans == prevuans:
       gc=gc-1
      if (usrans+"\n") == AL[qaindex]:
       print ("\n", usrans, " \nCorrect Answer!!!")
       CAC=CAC+1
       c=1
       break
    if c != 1:
     print ("\nAnswer was: ", AL[qaindex])
    QL.pop(qaindex)
    AL.pop(qaindex)
    input("Press Enter for next Question")
    os.system("clear")

  print ("Game Over!!!", CAC, "Answered Correct Out Of", QC)

main()
