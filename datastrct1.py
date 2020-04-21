import sys
import math
import random
import threading
import time
from functools import reduce

#--Binary search in a sorted lisst

"""
def binary_search(val,target):
    blen = len(val)
    val.sort()
    first = 0
    final = blen - 1
    mid = (first + final ) // 2
    while final >= first:
        if val[mid] == target:
            return mid
        elif val[mid] < mid:
            first = mid - 1 
            return first + 1
        elif val[mid] > mid:
            final = mid + 1
            return final + 1
        else:
            return "Value not found"
    
def main():
    lis = []
    print("Enter the number of elements for a list: ")
    n = int(input())
    print("Enter the values :")
    for i in range(0,n):
        ele = int(input())
        lis.append(ele)
    tar = int(input("Enter the number to find : "))
    res = binary_search(lis,tar)
    print("The position the value is present at ",(res+1))

print(main())

"""

import threading as th
import time

even = th.Event()
odd = th.Event()

def evenfunc():
    for i in range(0,30,2):
        print(i)
        odd.set()
        even.clear()
        even.wait()

def oddfunc():
    odd.wait()
    for i in range(1,20,3):
        print(i)
        even.set()
        odd.clear()
        odd.wait()
