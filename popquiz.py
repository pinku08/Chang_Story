'''print out a random number between -5 and 5'''

import random 

x=random.randint(-5,5)
print(x)



'''print out a random integer between 0 and 100 500'''

for i in range(500):
    y=6
    print(y)
    
'''print out a random number and determine if it is even or odd'''

s=random.randint(1,100)
if (x%2==0):
    print("The number " +str(x)+ "this is even!!")
else: 
    print("The number " +str(x)+ "this is odd!!")

'''print 100 random numbesr and determine if it is even or odd along the'''
for i in range(10):
    s=random.randint(1,100)
    if (x%2==0):
        print("The number " +str(x)+ "this is even!!")
    else: 
        print("The number " +str(x)+ "this is odd!!")
        
'''Notify the code in part 4 that will ADD up the number of Even numbers and print that results. ***Hint:use an accumulator variable***'''
acc=0
for i in range(10):
    s=random.randint(1,100)
    if (x%2==0):
        print("The number " +str(s)+ "this is even!!")
        acc+=1 #This is the same as  "acc=acc+1"
    else: 
        print("The number " +str(s)+ "this is odd!!")
        
print('The number of vens was' +str(acc))

'''New topic! write the same block of code ina function'''
