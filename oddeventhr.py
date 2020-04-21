#!/usr/bin/python

import threading
import random
import time
    # def run(self):
    #     oddeven.num()

def numb(i):        
        if i % 2 == 0:
            print("value {} is even !!".format(i)) 
def numdodd(i):
        if i % 2 != 0:
            print("value {} is Odd  ! ".format(i))
    

for i in range(1,15):
    thread = threading.Thread(target=numb, args=(i,))
    thread2 = threading.Thread(target=numdodd, args=(i,))
    thread.start()
    time.sleep(2)
    #if we put the thread here At first it will
    #it will execute the num even function and steeps after 
    #it's done once and execute the next function.
    thread2.start()
# print("Active Threads :", threading.activeCount())
 
#     # Returns a list of all active thread objects
# print("Thread Objects :", threading.enumerate())
print("Program COmpleted!")
