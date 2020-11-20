#!/usr/bin/python3
import random
money = 1000
while True:
    x = random.randint(1 ,6)
    y = random.randint(1 ,6)
    c = x + y
    if c ==7 or c == 11:
        print('you are the winner')
    elif c == 2 or c == 3 or c == 12:
        print('you are the loser')
    else:

