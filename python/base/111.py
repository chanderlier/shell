def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


def is_prime(num):
    for factor in range(2, int(num ** 0.5) +1):
        if num % factor == 0:
            return False
    return True if num != 1 else False


if __name__ == '__main__':
    num = int(input('please enter a number: '))
    if is_palindrome(num) and is_prime(num):
        print('%d is huiwensushu' % num)
    else:
        print('%d is not huiwensushu' % num)
