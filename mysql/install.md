```sh
rpm -ivh http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm
```
```sh
yum -y install mysql-community-server
```
```sh
systemctl enable mysql
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