def gcd(x,y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x,0,-1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x,y):
    return x *y // gcd(x,y)

if __name__ == '__main__':
    x = int(input('x='))
    y = int(input('y='))
    print('zdgys:',gcd(x,y))
    print('zxgbs',lcm(x,y))
    #lcm(x,y)
