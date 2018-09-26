'''This is all about functions'''

def greeting():
    print("holla")
    
#call the functions

greeting()

def name():
    name=input("what is your name") 
    return name
    
def askAge(): #write a function that ask and return how old they are   
    age=input("How old are you?")
    return age
    
def canVote(): #write a function that takes their age 18  and responds  #appropriately if they can or cannot vote
    if (age >=18):
        print("you can vote")
    else: 
        print ('you cannot vote')
    return canVote
    
#call the function
greeting()
x= askName() #save the output of askName() to variable
print ("Hello," + name)
y= askAge()
print(canvote(y))

#call the funcion and save the age to a vari