import random,os

def hints(r,g,gc) :
    print ('Hints are ')
    low=r-(r//8)
    high=r+(r//5)
    if low<0:
      low=0
    if high>2000:
      high=2000
    if gc==8:
      print ('1. Number is '+str(len(str(r)))+' digit number ')
      int(r)
    if gc<8:
      print('2. Number is in between',low,'and',high)
    if gc<8:
      if r%2==0 :
        print ('3. Number is even ')
      else :
          print ('3. Number is odd')
    rdnum=r
    d=3
    l=[]
    c=6
    while True and c!=0:
         if (rdnum % d)==0 :
           l.append(str(d))
           c-=1
           d+=1
         else :
             d+=1

    if gc!=8:
        if  g<r and (r-g)<=10 :
          print ('4. Number is higher than your guess (Diffrence is in between 0 and 10)')
        elif g<r and (r-g)>10 and (r-g)<50 :
            print ('4. Number is higher than your guess (Diffrence is in between 10 and 50)')
        elif g<r and (r-g)>50 :
            print ('4. Number is higher than your guess (Diffrence is grater than 50)')
        elif  g>r and (g-r)<=10: 
            print ('4. Number is lower than your guess (Diffrence is in between 0 and 10)')
        elif g>r and (g-r)>10 and (g-r)<50 :
            print ('4. Number is lower than your guess (Diffrence is in between 10 and 50)')
        elif g>r and (g-r)>50:
            print ('4. Number is lower than your guess (Diffrence is grater than 50)')



    temp=[]
    if gc<7:
        for i in range(0,7-gc):
         temp.append(l[i])
        print ("5. Number is divisible by ", temp)


def checkguess(rand):
    gcount=8
    print ('Enter guess in between 0 and 2000')
    while gcount!=-1:
         if gcount==0:
           print ('Guesses over !! ')
           print ('you lose !!! ')
           print ('Number was : ',rand)
           break
         guess=int(input('Enter your guess : '))
         os.system("clear")
         print ('Guess : ',guess)
         if gcount==0:
           print ('Guesses over !! ')
           print ('you lose !!! ')
           print ('Number was : ',rand)
           break
         if rand==guess:
           print ('Congrats !!!  your guess is correct . ')
           break
         else:
             if gcount!=1:
               hints(rand , guess ,gcount)
             gcount-=1
             if gcount!=0:
               print('guesses left',gcount)


def main():
    while True :
         randnum=random.randint(0,2000)
         checkguess(randnum)
         choice=input('\n Do you want to continue ?  [ y / n ] : ')
         print ('\n\n')
         if choice!='n' :
           continue
         else :
             break





main()
