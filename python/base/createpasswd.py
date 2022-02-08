#!/usr/bin/env python

from random import choice
import string

passwd_length = int(input('请输入要生成的密码长度：'))
passwd_count = int(input('请输入要生成几组密码：'))

# 通过string.punctuation获取所有的字符 如：'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
symbols = string.punctuation
# 通过string.digits 获取所有的数字的字符串 如：'0123456789'
number = string.digits
# 通过string.ascii_letters 获取所有英文字符的大小写字符串 'a..zA..Z'
Letter = string.ascii_letters
# 定义生成密码是组成密码元素的范围   字符+数字+大小写字母
passwd = symbols + number + Letter
password = number + Letter


def generate_passwd(*args, **kwargs):
    passwd_lst = []
    while (len(passwd_lst) < passwd_length):
        passwd_lst.append(choice(passwd))   # 把循环出来的字符插入到passwd_lst列表中
    return ''.join(passwd_lst)              # 合并列表中的所有元素组成新的字符串


def generate_password(*args, **kwargs):
    passwd_lst = []
    while (len(passwd_lst) < passwd_length):
        passwd_lst.append(choice(password))   # 把循环出来的字符插入到passwd_lst列表中
    return ''.join(passwd_lst)              # 合并列表中的所有元素组成新的字符串


if __name__ == '__main__':
    for i in range(0, passwd_count):
        print(generate_password())
