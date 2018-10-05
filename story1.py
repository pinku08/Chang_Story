
import time
from colorama import Fore, Back, Style

#this is are python story

def ask():#this is choice number 1 of whether uou want to do the mission of saving a dog or not
    ask=str(input("Do you accept this" + Fore.RED + " mission?" + Fore.RESET+"\'type yes or no\' "))
    if (ask == "yes" or ask == "Yes" ) :
        ask = True
        print(Back.CYAN + "Your mission is to save a dog from a well." + Back.RESET)
        print("Go find supplies to save dog ")
    elif(ask == "no" or ask == "No" ):
        ask = False
        print("Go get some dinner. ")
    return ask
    
def choice1():
    x=str(input("What do you get a bucket and rope or a firefighter? \'type bucket and rope or firefighter:\' "))
    if (x == "bucket and rope"):
        print ("What type of transportation?")
    elif (x == "firefighter"):
        exit("You failed. It is the fire season, they are busy. ")
    else:
        print("You can't type. You failed ")
    return x    
    
def transportation():#who want to take a taxi 
    t=str(input("What transportation do you want?\'type taxi or bus:\' "))
    if (t == 'bus'):
        print("What type of knots?")
    else:
        exit("You failed. It is dirty you got sick and died ")
    return t
    
def bus():#i dont even know what a double hitch is
    b=str(input("Double hitch or double knot: \'type Double hitch or double knot\'"))
    if (b == "Double hitch"):
        print("You saved the dog. You win!!!")
    else:
        exit("You failed. It is not strong enough.")
    return b

def eat():#every hour goes by you get a hour closer to your next pizza.... This code is asking them what they want to eat :)
    a=str(input("Chipotle or Pizza Hut? \'type pizza hut or chipotle\' "))
    if a==("pizza hut"):
        print("What types of flavor do you want? \'meat lover or cheese\'  ")
    else:
        print('You got diarrhea and failed.')
        return a

def dog():
    bog=str(input("(hint you are lactose intolerance) "))
    if bog==("meat lover"):
        print("Good pick let's go get a dog.")
    else:
        print("You failed :(")
        return bog

def store():
    p=str(input("Where do you want to go petco or a sketchy van\' type petco or van \' "))
    if p==("petco"):
        print("you get a normal dog yay!")
    elif p==("van"):
        print("You get a dog with super powers YAY! ")
        return p

ask  = ask()
if(ask == True):
    choice1()
    transportation()
    bus()

if(ask == False):       
    print("Let's go buy some food to eat. ")
    a = eat()
    dog()
    store()
exit = input("If you would like to end this program, press enter.")

    