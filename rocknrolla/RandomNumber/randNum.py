import os,random

def check(randNum,guessNum,gc):
  if randNum==guessNum:
   return 0
  if gc<3:
   if (randNum%2)==0:
    print ("Number is Even")
   else:
    print ("Number is Odd")
  if guessNum>randNum:
   print ("Your Number is High")
  else:
   print ("Your Number is Low")
  if abs(randNum-guessNum)>50:
   print ("You are far away")
  elif abs(randNum-guessNum)>10:
   print ("You are close")
  else:
   print ("You are very close")
  return 1 
   

def main():
  gc=8
  randNum=random.randint(0,2000)
  print ("Guess The Number \nInitial Hints\nMaximum number is 2000")
  if randNum<1000:
   print ("Number is below 1000")
  else:
   print ("Number is above or equal to 1000")

  for i in range(0,gc):
    print ("You have ",gc," Guesses ")
    guessNum=int(input("Enter Guess: "))
    os.system("clear")
    stat=check(randNum,guessNum,gc)
    if stat==0:
     break
    gc-=1

  if stat==0:
   print ("Congrats!!! You Guessed Correct Number: ",randNum)
  else:
   print ("OOOPSSS!!! You are out of Guesses, Number was: ",randNum)


main()
