mysql备份除了mysqldump，还可以通过xtrabackup来实现备份。但mysqldump无法实现对数据库进行增量备份，在实际生产环境中增量备份却上是非常实用的。
## Xtrabackup优点
（1）备份速度快，物理备份可靠
（2）备份过程不会打断正在执行的事务（无需锁表）
（3）能够基于压缩等功能节约磁盘空间和流量
（4）自动备份校验
（5）还原速度快
（6）可以流传将备份传输到另外一台机器上
（7）在不增加服务器负载的情况备份数据
## 安装Xtrabackup
```sh
yum install -y https://repo.percona.com/yum/percona-release-latest.noarch.rpm
percona-release enable-only tools release
yum install percona-xtrabackup-80 -y
```
或者
```sh
wget https://www.percona.com/downloads/XtraBackup/Percona-XtraBackup-8.0.4/binary/redhat/7/x86_64/percona-xtrabackup-80-8.0.4-1.el7.x86_64.rpm
yum localinstall percona-xtrabackup-80-8.0.4-1.el7.x86_64.rpm
```
安装qpress
```sh
yum install qpress
```
卸载
```sh
yum remove percona-xtrabackup
```