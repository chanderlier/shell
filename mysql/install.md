```sh
rpm -ivh http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm #mysql5.7
rpm -ivh http://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm #mysql8.0
```
```sh
yum -y install mysql-community-server
```
```sh
systemctl enable mysqld
```
```sh
systemctl start mysqld
```
```sh
grep "password" /var/log/mysqld.log
```

mysql57
mysql -uroot -p
set password = password('newpassword')

grant all privileges on *.* to root@"%" identified by "newpassword";
flush privileges;

mysql80
mysql -uroot -p
