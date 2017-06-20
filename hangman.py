#hangman game
import os
import random

## Actual game function
def hangman (questns,questionsAsked,count):
    guesses = 6
    questions = list()
    guessList = list()

    os.system('clear')
    while True:
        if len(questionsAsked) == count:
            print("WOW! You've played 'em ALL!")
            print("See ya Later!")
            exit()

        qNo = random.randint(0,count-1)
        if qNo not in questionsAsked:
            questionsAsked.append(qNo)
            break

    answer = questns[qNo][1].upper()

    flag=1
    while guesses and flag==1:
        os.system('clear')

        print ("\nQuestion 1:")
        print (questns[qNo][0])
        flag =0

        for a in answer:
            if a == ' ':
                print (a,end=" ")
            elif a in guessList:
                print (a.upper(),end=" ")
            else:
                flag=1
                print ("_",end=" ")

        if flag ==0:
            continue

        print("\n\nYour initial Guesses: ",guessList)
        print("Gueses Left: ",guesses)
        g = input("\n\nEnter Guess: ").upper()

        while True:
            if len(g)!=1:
                print("Enter Single character only!")
                g = input("\nEnter Guess: ").upper()
            else:
                break

        while g in guessList:
            print("\n Character Already Guessed! Please Try Again.")
            g = input("\nEnter Guess: ").upper()

        guessList.append(g)

        if g not in answer:
            guesses -=1
            if guesses == 0:
                print("OOPS! You're out of guesses!")
                print("The correct answer is", answer.upper())
                #print("Hope To See You Back soon!\n")
                # exit()
                return


    print("\nCongratulations! Correct Answer!!!")

## Caller's code

questionsAsked = list()
questions = list()
count = 0
try:
    fileHandler = open("hangman.txt","r")

    for ques in fileHandler:
        ques = ques.rstrip()
        QnA = tuple(ques.split(':'))
        questions.append(QnA)
        count += 1
except FileNotFoundError:
    print("hangman.txt not found.")
except IOError:
    print("Cannot Open hangman.txt.")
finally:
    fileHandler.close()

    hangman(questions,questionsAsked,count)

    while True:
        c = input("Want to play again?(Y/N) ")
        if c == 'Y' or c== 'y':
            hangman(questions,questionsAsked,count)
        else:
            print("\nHope to see you back soon!\n")
            exit()
