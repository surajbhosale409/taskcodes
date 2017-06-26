import os,random

def check(ans,Templ,guess):
      for x in guess:
         i=0
         while i<len(ans):
              j=ans.find(x,i)
              l=list(Templ)
              if j!=-1:
                l.pop(j)
                l.insert(j,x)
              i+=1
              Templ="".join(l)
      return Templ
def askguess(Ql,Al,s):
    gcount=len(Al)
    Templ=['_' * (len(Al)) ]
    print (Ql)
    print (Templ[0])
    guess=input('Enter your guess : ')
    if guess.islower():
      guess=guess.upper()
    print ('guesses left : ',gcount)
    gcount-=1
    Templ=check(Al,Templ[0],guess)
    while ((gcount!=0) and (Templ!=Al)):
          print (Ql)
          print (Templ)
          print ('guesses left : ',gcount)
          guess=input('Enter your guess : ')
          if guess.islower():
            guess=guess.upper()
          Templ=check(Al,Templ,guess)
          gcount-=1
    if (Templ==Al) :
        print (Templ)
        print ('correct answer !! ')
        s+=1
    else :
         print (Templ)
         print ('Gusses over !! ')
    return s



def main():
    Ql=['What is the capital of India ? ','Which is the largest mountain in Maharashtra ?','Who is the inventor of c ?','Who is the prime minister of India ?','Who is the captain of indian ceicket team ? ','Who is the first prime minister of India ?','Economical capital of India ?']
    Al=['DELHI','KALSUBAI','DENNIS RITCHIE','NARENDRA MODI','VIRAT KOHLI','JAWAHARLAL NEHRU','MUMBAI']
    score=0
    for x in range(len(Ql)):
       os.system("clear")
       score=askguess(Ql[x],Al[x],score)
       choice=input('Do you want to continue [y/n] :')
       if choice=='n':
         break
    print ('Your score is : ',score)


main()
