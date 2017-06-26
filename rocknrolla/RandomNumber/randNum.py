import os,random


def initHints(randNum):
  iniHints=[]
  iniHints.append("Initial Hints:")
  iniHints.append("Is a "+str(len(str(randNum)))+" digit number")
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
  itrHints.append("Hints from previous guess:")
  if guessNum>randNum:
   itrHints.append("Your Number is High")
  else:
   itrHints.append("Your Number is Low")
  if abs(randNum-guessNum)>50:
   itrHints.append("You are far away (difference is greater than 50)")
  elif abs(randNum-guessNum)>10:
   itrHints.append("You are close!!! (difference is between 10-50)")
  else:
   itrHints.append("You are very close!!! (difference is less than 10)")
  return itrHints  
    

def main():
  stat=1
  while True:
   c=gc=8
   itrHints=[]
   randNum=random.randint(0,2000)
   for i in range(0,c):
     os.system("clear")
     print ("Guess The Number")
     iniHints=initHints(randNum)
     ind=0
     for hint in iniHints:
      if ind!=0:
       print ("[",ind,"] ",hint)
      else:
       print(hint)
      ind+=1
     ind=0
     for itrHint in itrHints:
       if ind!=0:
        print ("[",ind,"] ",itrHint)
       else:
        print(itrHint)
       ind+=1
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
