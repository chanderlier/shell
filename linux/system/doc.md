查看哪个经常使用的fd最多
```sh
find /proc -print |grep -P '/proc/\d+/fd/'|awk -F  '/' '{print $3}'|uniq -c |sort -rn |head
```
```sh
lsof -p pid
```
```sh
ll /proc/pid/fd
```
```sh
cat /proc/net/tcp |grep socket
```
将十六进制转换为IP地址
```
ss -ntp
```