'''
1 for snake
-1 for water
0 for gun
'''
# Took the help of chatgpt for generating random number from compuiter's side.

import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youDict[youstr]

print(f"You chose {reverseDict[you]} and Computer chose {reverseDict[computer]}")

if(computer == you):
    print("TIE!!")

elif(computer == -1 and you == 1):
    print("YOU WIN!!")

elif(computer == -1 and you == 0):
    print("YOU LOSE!!")

elif(computer == 1 and you == 0):
    print("YOU WIN!!")

elif(computer == 1 and you == -1):
    print("YOU LOSE!!")

elif(computer == 0 and you == 1):
    print("YOU LOSE!!")

elif(computer == 0 and you == -1):
    print("YOU WIN!!")
    
else:
    print("Something went wrong..")