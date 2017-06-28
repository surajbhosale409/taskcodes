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
    gcount=(len(Al)-1)
    Templ=['_' * (len(Al)) ]
    print (Ql,'\n')
    print (Templ[0])
    guess=input('\n Enter your guess : ')
    os.system("clear")
    if guess.islower():
      guess=guess.upper()
    #print ('\n guesses left : ',gcount,'\n')
    #gcount-=1
    Templ=check(Al,Templ[0],guess)
    while ((gcount!=0) and (Templ!=Al)):
          print ('\n',Ql,'\n')
          print (Templ)
          print ('\n guesses left : ',gcount)
          guess=input('\n Enter your guess : ')
          os.system("clear")
          if guess.islower():
            guess=guess.upper()
          Templ=check(Al,Templ,guess)
          gcount-=1
    if (Templ==Al) :
        print (Templ)
        print ('\n correct answer !! ')
        s+=1
        print ('\n Your score is : ',s)
    else :
         print (Templ)
         print ('\n Gusses over !! ')
         print ('\n Correct Answer was : ',Al,'\n')
    return s



def main():
    Ql=['Who is the developer of linux operating system','What is the capital of India ? ','Which is the largest mountain in Maharashtra ?','Who is the inventor of c ?','Who is the prime minister of India ?','Who is the captain of indian ceicket team ? ','Who is the first prime minister of India ?','Economical capital of India ?']
    Al=['LINUS TORWALDS','DELHI','KALSUBAI','DENNIS RITCHIE','NARENDRA MODI','VIRAT KOHLI','JAWAHARLAL NEHRU','MUMBAI']
    score=0
    for x in range(len(Ql)):
       os.system("clear")
       score=askguess(Ql[x],Al[x],score)
       choice=input('\n Do you want to continue [y/n] :')
       print ('\n')
       if choice=='n':
         break
    print ('\n Your score is : ',score,'\n')


main()
