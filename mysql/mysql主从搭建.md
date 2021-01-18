|  host |  hostname | system-release  | mysql-version  |
| ------------ | ------------ | ------------ | ------------ |
|  192.168.2.92 |slave   |Alibaba Cloud Linux (Aliyun Linux) release 2.1903 LTS   | mysql-8.0.22  |
|  192.168.2.94 |  master |  CentOS Linux release 8.1.1911 (Core) |  CentOS Linux release 8.1.1911 (Core) 
 |

master
启动mysql后，可以去默认的/var/lib/mysql目录下，确认是否开启binlog
```sh
ls /var/lib/mysql/
```
如果有binlog.000001的话，只需要在下面的文件，添加server-id即可
cat /etc/my.cnf.d/mysql-server.cnf
```sh
[mysqld]
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock
log-error=/var/log/mysql/mysqld.log
pid-file=/run/mysqld/mysqld.pid
server-id=1
```
```sh
mysql -uroot -p
```
```sh
mysql>create user 'repl'@'%' identified by 'password';
mysql>grant replication slave on *.* to 'repl'@'%';
mysql>flush privileges;
mysql>show master status;
```
```sh
-+
| File          | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+---------------+----------+--------------+------------------+-------------------+
| binlog.000003 |     2963 
```
记录binlog.000003 和2963

slave
对配置文件进行修改前，建议先备份
```sh
cp /etc/my.cnf /etc/my.cnf.bk
```
修改完的配置文件，大致如下
```sh
cat /etc/my.cnf
```
```sh
server-id=2
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock
log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid
```
确保master和slave在局域网内的server-id不同
```sh
mysql -uroot -p
```
```sh
mysql>change master to master_host='192.168.2.94',master_port=3306,
master_user='repl',master_password='password',
master_log_file='binlog.000003',master_log_pos=2963;
mysql>show slave status\G;
mysql>start slave;
mysql>show slave status\G;
```