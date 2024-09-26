'''
water = -1
snake = 1
gun = 0 
'''

import random

computer = random.choice(-1,1,0)

youstr = input("Enter your choice: ")
youdict = {"W":-1 , "S":1 , "G":0}
reversedict = {-1 :"Water", 1:"Snake" , 0:"Gun"}
you = youdict[youstr]

print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

if(computer == you):
    print("It's a draw!")
else:
    if(computer == -1 and you == 1):
        print("You Won!")
    elif(computer == 1 and you == 0):
        print("You Won!")
    elif(computer == 0 and you == -1):
        print("You Won!")
    elif(computer == 1 and you == -1):
        print("You Lose!")
    elif(computer == -1 and you == 0):
        print("You Lose!")
    elif(computer == 0 and you == 1):
        print("You Lose!")
    else:
        print("Something went wrong!")