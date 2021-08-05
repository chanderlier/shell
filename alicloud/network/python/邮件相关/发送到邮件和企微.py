import sys
import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email_msg(result, branch, pname, domian, email, paddr, oss_addr, api_type):
    # SMTP 服务
    mail_host = "smtp.exmail.qq.com"  # 设置服务器
    mail_user = "user@email.com"  # 用户名
    mail_pass = "passworld"  # 口令
    receivers = [email, 'receivers@email.com']

    text = """
    Gitlab-CI 自动发布结果通知, 详细信息如下:

     - 发布结果: %s

     - 分支: %s

     - 项目名: %s

     - 项目域名: %s

     - 提交用户: %s

     - 项目地址: %s

     - OSS地址: %s

        """ % (result, branch, pname, domian, email, paddr, oss_addr)

    msg = MIMEText(text, 'plain', 'utf-8')
    msg["Subject"] = Header("[%s]自动部署结果通知" % pname, 'utf-8')
    msg["From"] = 'receiver@email.com'
    msg["To"] = email
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(mail_user, receivers, msg.as_string())
        print("Send Mail Success")
        return True
    except Exception as e:
        print(e)
        print("Error: Send Mail Faild")
        return None


def send_qyweixin_msg(result, branch, pname, domian, email, paddr, oss_addr, api_type):
    color = 'green' if result == '成功' else 'red'
    templates = """
#### [%s]自动部署结果通知:
 - 发布结果: <font color=\"%s\">  %s </font>

 - 分支: %s

 - 项目名: %s

 - 项目域名: %s

 - 提交用户: %s

 - 项目地址: %s

 - OSS地址: %s
    """ % (pname, color, result, branch, pname, domian, email, paddr, oss_addr)
    send_message_by_qyapi(templates, email, api_type)


def send_message_by_qyapi(content, mentionor, api_type):
    qyapi = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxxxxxxxxxxxxxxx'
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": content,
            "mentioned_list": [mentionor]
        }
    }
    res = requests.post(url=eval(api_type), json=data)
    print(res.text)


if __name__ == "__main__":
    args = sys.argv[1:]
    send_email_msg(*args)
    send_qyweixin_msg(*args)
