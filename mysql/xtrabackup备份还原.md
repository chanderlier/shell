install
5.7
```sh
yum install https://repo.percona.com/yum/percona-release-latest.noarch.rpm
```
```sh
wget https://www.percona.com/downloads/XtraBackup/Percona-XtraBackup-2.4.4/\
binary/redhat/7/x86_64/percona-xtrabackup-24-2.4.4-1.el7.x86_64.rpm
```
```sh
yum localinstall percona-xtrabackup-24-2.4.4-1.el7.x86_64.rpm
```
```sh
percona-release enable tools
```
```sh
yum install qpress
```
xtrabackup可以在不加锁的情况下备份innodb数据表，不过此工具不能操作myisam。
innobackupex是一个封装了xtrabackup的脚本，能同时处理innodb和myisam，但在处理myisam时需要加一个读锁。

全量备份
innobackupex
```sh
innobackupex --defaults-file=/etc/my.cnf --user=root --password='passwd' /mnt/mysql/backup/all-backup
```
xtrabackup
准备备份
```sh
xtrabackup --prepare --target-dir=/data/compressed/
```
```sh
xtrabackup --backup --compress --target-dir=/data/compressed/
```
加快速度，并行压缩
```sh
 xtrabackup --backup --compress --compress-threads=4 --target-dir=/data/compressed/
```
解压
```sh
xtrabackup --decompress --target-dir=/data/compressed/
```
```sh
systemctl stop mysqld
```

全量还原
```sh
xtrabackup --copy-back --target-dir=/data/backups/
```
调整权限（如有必要）
```sh
chown -R mysql:mysql /var/lib/mysql
```

测试 10:52
180G的mysql数据库，使用压缩备份，需要30分钟，备份后的目录大小为41G