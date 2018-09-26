'''New topic! write the same block of code ina function and call that function 10 times'''
def EvenOdd(): #insert directions below
    import random
    acc=0
    for i in range(10):
        s=random.randint(1,100)
        if(s%2==0):
            print("The number " +str(s)+ "this is even!!")
            acc+=1 #This is the same as  "acc=acc+1"
        else: 
            print("The number " +str(s)+ "this is odd!!")
            
    print ('The number of vens was' + str(acc))
    
def greeting():
    x=input('Please enter your name:')
    print("Hello " +str(x) + " Nice to meet you!")
    
def age():
    age=int(input('How old are you?'))
    return age

  