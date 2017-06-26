import os,random


def initHints(randNum):
  iniHints=[]
  iniHints.append("Is a "+str(len(str(randNum))))
  lowLim=randNum-(randNum//10)
  upLim=randNum+((randNum//10)//10)+20
  if lowLim<0:
   lowLim=0
  if upLim>2000:
   upLim=2000
  iniHints.append("Number is between "+str(lowLim)+" - "+str(upLim))
  if randNum%2==0:
   evnodd="Number is even"
  else:
   evnodd="Number is odd"
  iniHints.append(evnodd)
  return iniHints


def check(randNum,guessNum,gc):
  itrHints=[]
  
  if guessNum>randNum:
   itrHints.append("Your Number is High")
  else:
   itrHints.append("Your Number is Low")
  if abs(randNum-guessNum)>50:
   itrHints.append("You are far away (difference is greater than 50)")
  elif abs(randNum-guessNum)>10:
   itrHints.append("You are close!!! (difference is between 10-50)")
  else:
   itrHints.append("You are very close!!! (difference is less than 10")
  return itrHints  
    

def main():
  while True:
   c=gc=8
   itrHints=[]
   randNum=random.randint(0,2000)
   for i in range(0,c):
     os.system("clear")
     print ("Guess The Number \nInitial Hints")
     iniHints=initHints(randNum)
     for hint in iniHints:
      print (hint)
     for itrHint in itrHints:
      print (itrHint)
     print ("You have ",gc," Guesses ")
     if gc!=8:
      print ("Previous Guess is ",prevGuess)
     prevGuess=guessNum=int(input("Enter Guess: "))
     
     if guessNum==randNum:
      stat=0
      break
     gc-=1
     itrHints=check(randNum,guessNum,gc)   

   if stat==0:
    print ("Congrats!!! You Guessed Correct Number: ",randNum)
   else:
    print ("OOOPSSS!!! You are out of Guesses, Number was: ",randNum)
   ch=input("Play Again (Y/N)")
   if ch=='N' or ch == 'n':
    break
      
main()
