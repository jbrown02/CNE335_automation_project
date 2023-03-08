# Joshua Brown
# 3/7/23
# CNE 335 Winter - Final Project

def print_program_info():
    print("Server Automator v0.1 by Josh Brown")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()

from Server import Server
import os

def myping(host):
    response = os.system("ping -c 1 " + host)
    
    if response == 0:
        return True
    else:
        return False
        
print(myping("54.245.39.214"))
