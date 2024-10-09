import random
import os
choice =1
while choice:
    num=random.randint(1,6)
    print(f"dice shows the number : {num}\n")
    choice=int(input("Enter 0 to exit or 1 to Roll the dice again\n"))
    os.system('cls')