#!/usr/bin/python3
from random import randint
money = 1000

while money > 0:
    print('your money:',money)
    needs_go_on = False
    while True:
        debt = int(input('please xiazhu :'))
        if 0 < debt <= money:
            break
    first = randint(1,6) + randint(1,6)
    print('player get number%d point' % first)
    if first == 7 or first == 11:
        print('you are the winner')
        money += debt
    elif first == 2 or first == 3 or first ==12:
        print('you are the loser')
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1,6) + randint(1,6)
        print('player got number %d point' % current)
        if current ==7:
            print('you are the  loser')
            money -= debt
        elif current == first:
            print('you are the winner')
            money += debt
        else:
            needs_go_on = True
print('game over!')
