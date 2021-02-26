import random
a = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('please enter a number: '))
    if number < a:
        print('dayidian')
    elif number > a:
        print('xiaoyidian')
    else:
        print('correct')
        break
print('ni zongcail%dci' % counter)
