查看 mysql 初始的密码策略
```sql
SHOW VARIABLES LIKE 'validate_password%';
```
设置密码策略为LOW
```sql
set global validate_password_policy=LOW;
```
