import random,os,math

def start():
    """The program starts from here"""

    choice ='Y'
    # print("What to do?\n The Computer has selected a number at random.")
    # print("Your job is to guess that number!")
    # choice = input("Want to play? (Y/N)").upper()
    # while choice != 'Y' and choice != 'N':
    #     choice = input("Want to play? (Y/N)").upper()

    if choice=='Y':
        pickNumber()
    else:
        print ("See you soon!")
        exit()

def pickNumber():
    """Computer picks a number"""

    number=random.randint(0,1000)
    hints=generateHint(number)

    startGuessing(hints,number)

    choice = input("Want to play? (Y/N)").upper()
    while choice != 'Y' and choice != 'N':
        choice = input("Want to play? (y/n)").upper()

    if choice=='Y':
        pickNumber()
    else:
        print ("\nSee you soon!")
        exit()

def generateHint(number):
    """Generates a hint for the number"""
    divisible = range(2,int(math.sqrt(number)))
    hint =list()

    digits = len(str(number))
    hint.append(str(digits)+" digit number")

    mod = number%(10**(digits-1))
    r1  = number - mod
    if mod > 50:
        r1  = (number-mod) + 50

    r2 = r1+50
    hint.append("Number is between "+str(r1) +", "+str(r2))

    divi = list(filter(lambda x: number%x==0,divisible))
    if len(divi)==0 :
        hint.append("Number is Prime")
    else:
        hint.append("Number is divisible by "+str(divi))

    return hint

def startGuessing(hints,number):
    guesses = 5
    msg = ""
    while guesses:
        try:
            os.system("clear")

            i=1
            for hint in hints:
                print ("["+str(i)+"]. ",hint)
                i+=1

            print ("Guesses Left: ",guesses)
            print (msg)

            guess = int(input("Enter Guess: "))

            if guess == number:
                print ("CORRECT ANSWER!! The Number is",number)
                return
            else:
                guesses-=1
                difference = abs(number - guess)
                if difference > 10:
                    msg = "You're guess is pretty far from the original number!"
                elif difference >5:
                    msg = "You're close to the original number"
                else:
                    msg = "You're very close!!"




        except:
            input("\nError! Please Enter a number. (Press enter to continue.)")

    print ("OOPS! You're out of guesses!! \nThe number was",number)


start()
