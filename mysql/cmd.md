查看 mysql 初始的密码策略
```sql
SHOW VARIABLES LIKE 'validate_password%';
```
设置密码策略为LOW
```sql
set global validate_password_policy=LOW;
```

导出指定表的数据
以下命令都会锁表
```sh
mysqldump -t database -u username -ppassword --tables table_name1 table_name2 table_name3 > /data/mysql/db.sql
```
导出指定表的结构
```sh
mysqldump -d database -u username -ppassword --tables table_name1 table_name2 table_name3>/data/mysql/db2.sql
```
导出指定表的数据和结构
```sh
mysqldump  database -u username -ppassword --tables table_name1 table_name2 table_name3>/data/mysql/db3.sql
```
导出除了部分表之外所有的表
```sh
mysqldump  -u username -ppassword --default-character-set=utf8 --database database_name --ignore-table=database_name.table_name1
--ignore-table=database_name.table_name2 
--ignore-table=database_name.table_name3 >/data/mysql/db4.sql
```