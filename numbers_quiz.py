'''
Pop Quiz: Use a FOR loop for the following program.

Level 1: 
Write a computer program that will count down from 10.

Level 2: 
Modify the program so that it will count down from whatever number the user decides.

Level 3: 
Modify the program so that it delays 1 second using the package "time" and the method time.sleep(1) inside the loop.
'''
import time 
# level 1
for x in range(10, -1,-1):
 print (x)
 time.sleep(1)
#level 2
x=input ("Please count to zero:")
for x in range (int(x),-1,-1):
    time.sleep(1)
    print(x)
 

       
   
 