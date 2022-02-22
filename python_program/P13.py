"""13). Please write a program to output a random number, 
which is divisible by 5 and 7,  between 0 and 10 inclusive
 using random module and list comprehension."""


import random

print(random.choice([i for i in (0,10) if i%7==0 and i%5==0]))