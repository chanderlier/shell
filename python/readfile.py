import time 

def main():
    try:
        with open('studypython/text.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知编码的!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    
    with open('studypython/text.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    with open('studypython/text.txt') as f:
        lines = f.readlines()
    print(lines)

if __name__ == '__main__':
    main()
