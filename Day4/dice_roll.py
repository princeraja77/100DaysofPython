import random
import os
import time
choice =1
while choice:
    num=random.randint(1,6)
    for i in range(10):
        print(f"dice shows the number : {num}",end=">>>>>>",flush=True)
        time.sleep(1)
    choice=int(input("Enter 0 to exit or 1 to Roll the dice again\n"))
    os.system('cls')
