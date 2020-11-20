import re


def main():
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''重要的事情说三遍，我的手机号是18888888888这个靓号，不是13444343535，也不是110或119，\
        小魔仙的才是13728283847'''
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------华丽的分割线--------')

    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------华丽的分割线--------')

    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


if __name__ == "__main__":
    main()
