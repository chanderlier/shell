import re

def main():
    username = input('please input your username:')
    qq       = input('please input your qq number:')
    m1       = re.match(r'^[0-9a-zA-Z_]\d{6,20}$', username)
    if not m1:
        print('please input effective username')
    m2 = re.match(r'^[1-9]\d{4-11}$', qq)
    if not m2:
        print('please input effective qq number')
    if m1 and m2:
        print('you have input effective info')

if __name__ == "__main__":
    main()