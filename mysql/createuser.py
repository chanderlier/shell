import pymysql
import random


def getpassword(length):
    pw = str()
    characters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM" \
        + "1234567890" + "!@#^&*,."
    for i in range(length):
        pw = pw + random.choice(characters)
    return pw


DBName = "dieser"
User = "dieser"
Password = getpassword(16)
conn = pymysql.connect(host="localhost", user="root", password="123456")

cursor = conn.cursor()

sql = "CREATE DATABASE IF NOT EXISTS  %s DEFAULT CHARACTER SET utf8mb4 \
    COLLATE utf8mb4_general_ci" % DBName
print(sql)
sql2 = "GRANT ALL PRIVILEGES ON %s.* TO %s@'172.16.%%' \
    IDENTIFIED BY '%s'" % (DBName, User, Password)
sql3 = "GRANT ALL PRIVILEGES ON %s.* TO %s@'192.168.%%' \
    IDENTIFIED BY '%s'" % (DBName, User, Password)
sql4 = "GRANT ALL PRIVILEGES ON %s.* TO %s@'10.0.%%' \
    IDENTIFIED BY '%s'" % (DBName, User, Password)
print(sql2)
sql5 = "flush privileges"
print(sql3)
print(Password)
cursor.execute(sql)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)
cursor.execute(sql5)
cursor.close()
conn.close()
