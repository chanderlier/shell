统计80端口连接数：

```sh
netstat -nat|grep -i "80"|wc -l
```
统计httpd协议连接数：
```sh
ps -ef|grep httpd|wc -l
```
统计状态为established的连接数：

```sh
netstat -na|grep ESTABLISHED|wc -l
```
按IP连接数排序：

```sh
netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n
```
统计nginx访问量前10的url：

```sh
cat /var/log/nginx/access.log | awk '{print $7}' | sort | uniq -c | sort -nr | head -n 10
```

统计访问次数前10的ip:

```sh
cat /var/log/nginx/access.log | awk '{print $1}' | sort | uniq -c | sort -nr | head -n 10
```
统计访问量前10的时间段：

```sh
cat /var/log/nginx/access.log |grep -P "\[{1}(.+)]" -o|cut -c 14-15|sort|uniq -c|sort -nr|head
```
