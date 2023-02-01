

# pe = 27

# taxi_price = pe * 3.600
# ff = str(taxi_price)

# print(taxi_price)
# print(type(taxi_price))
# print(ff)
# print(type(ff))







### load qilish 

import time
import replit
from random import randint
percent = 0
for i in range(12):
    replit.clear()
    percent +=1
    print("""
LOADING SCREEN
Status: loading

%"""+ str(percent)
         )
    time.sleep(randint(1,1))
    
print("Loading complete!\n")
print("Now...")
time.sleep(2)
print("What you have been waiting for...")
time.sleep(2)
print("Nothing")