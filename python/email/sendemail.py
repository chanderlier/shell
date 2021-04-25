# -*- coding: utf8 -*-
import sys
import os
import smtplib
import random
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header


def gen_user_vpn(email):
    src = string.ascii_letters + string.digits
    passwd = ''.join(random.sample(src, 16))
    gen_cmd = "/usr/bin/bash /opt/vpn/add_vpn_user.sh  '" + email + "'  '" + passwd + "'"
    print(gen_cmd)
    rcode = os.system(gen_cmd)
    if rcode == 0:
        return passwd
    else:
        print('create command faild')
        sys.exit(1)


def send_mail_with_files(email):
    passwd = gen_user_vpn(email)
    file_path = "/opt/vpn/docs/"
    files = [file_path + file for file in os.listdir(file_path)]

    # 第三方 SMTP 服务
    mail_host = "smtp.exmail.qq.com"  # 设置服务器
    mail_user = ""  # 用户名
    mail_pass = ""  # 口令
    receivers = [email, '']

    msg = MIMEMultipart()
    msg["Subject"] = Header("配置信息", 'utf-8')
    msg["From"] = 'm'
    msg["To"] = email

    # ---文字部分---
    name = email.split('@')[0]
    text = """
    Dear {}:
            
        欢迎使用免客户端VPN连接方式   
        
        服务器地址:
        
        预共享秘钥:
        
        用户: {}
        
        密码: {}

        安装配置请参考附件

        遇到问题请联系

    """.format(name, email, passwd)

    part = MIMEText(text, 'plain', 'utf-8')
    msg.attach(part)
    # 循环添加附件
    for file in files:
        part = MIMEApplication(open(file, 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=file.split('/')[-1])
        msg.attach(part)
    try:
        smtpObj = smtplib.SMTP_SSL()
        smtpObj.connect(mail_host, 465)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(mail_user, receivers, msg.as_string())
        print("Send Mail Success")
    except smtplib.SMTPException:
        print("Error: Send Mail Faild")


if __name__ == '__main__':
    email = sys.argv[1]
    send_mail_with_files(email)
