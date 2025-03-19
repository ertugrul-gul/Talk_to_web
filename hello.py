import math
import os
import random
import re
import sys

n = int(input("Bir sayi girinizi: "))

def give_integer(n):
    if n % 2 ==1:
        print ("Weird")
    elif 2<= n <= 5 and n % 2 == 0:
        print ("Not Weird")
    elif 6 <= n <=20 and n %2 == 0:
        print("Weird")
    elif n > 20 and n % 2 ==0:
        print ("Not Weird")

give_integer(n)




if name == 'main':
n = int(input().strip())
    if n%2==1:
        print("Weird")
    else: n>=2 and n<=5:
        print("Not Weird")
    elif n>=6 and n<=20:
        print("Weird")
    else: print("Not Weird")