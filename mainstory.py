def yes_or_no():
    YesNo = input("Yes or No?")
    YesNo = YesNo.lower()
    if(YesNo == "yes"):
        return 1
    elif(YesNo == "no"):
        return 0
    else:
        return yes_or_no()

yes_or_no()

if(yes_or_no() == 1):
    print("You said yeah!")
elif(yes_or_no() == 0):
    print("You said nah!")





















'''
gameExit= True
while (gameExit==True):
  x= int(input("Do you accept this mission?\'type yes or no\' "))
  if (x=="yes" or x== "Yes" ):
      print("Your mission is to save a dog from a well. ")
      print("Go get supplies to save dog ")
      break 
      print("You win")
  elif (x== "no" or x== "No" )
gameExit=False #over wright the value of gameFruit
  elif (x== "no" or x== "No" ):
    
      
          print("You are a loser")
          gameExit=True
          
        if (ask == "yes" or ask == "Yes" ) :
        print("Your mission is to save a dog from a well. ")
        print("Go get supplies to save dog ")
    elif (ask == "no" or ask "No")
    
    elif (ask == "no" or ask "No") 
    
    
    
    def false():
    false=str(input("Do you accept this mission?\'type yes or no\' "))
    if(false== "no" or false== "No"):
        def eat():
            false=str(input("Where would you go to eat:chipotle or pizza hut?\'type pizza hut or chipotle\'"))
            if false==("pizza hut"):
                print("What types of flavor do you want?\'meat lover or cheese\'")
            else:
                print('You got diarrea and failed.')
        
    '''