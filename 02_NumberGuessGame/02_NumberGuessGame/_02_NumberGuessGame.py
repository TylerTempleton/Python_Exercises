#The purpose of this app is to ask the user for a number between 0-100, evaluate the input and say if its higher/lower or that it is the correct number
#import random number generation

import random


# Title bar string
title = """
---------------------
Guess That Number
---------------------
"""

#try agian string
tryAgain = "Sorry not a valid number please try again"

#print Title
print(title)
#create random number
targetNumber = random.randint(0,100)
#initalize guess variable
guess = -1

#ask user for their name
name = input("What is your name?")
#boolean value to go till the number is found
while guess !=targetNumber:
    #test number to see if its a value int value
        try:
            guess_text = input("guess a number between 0-100: ")
            guess = int(guess_text)
            #not int value exception
        except ValueError:   
            print(tryAgain)
        
        
        #check guess value to target number value  
        else:
                 if guess < targetNumber:
                    print("Sorry {}, your guess of {} was too low." .format(name, guess))
                 elif guess > targetNumber:
                    print("Sorry {}, your guess of {} was too high." .format(name, guess))
                 else:
                    print('Awesome job {}, you win! The correct answer was {}' .format(name,guess))
                    
           
               
            
 
#end of game text
print("game over")