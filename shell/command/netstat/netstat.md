##统计80端口连接数：

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
```
netstat -an |wc -l
```
```
netstat -an |grep xx |wc -l        查看某个/特定ip的连接数
```
```
netstat -an |grep TIME_WAIT|wc -l    查看连接数等待time_wait状态连接数
```
```
netstat -an |grep ESTABLISHED |wc -l    查看建立稳定连接数量
```
 

查看不同状态的连接数数量
```sh
netstat -an | awk '/^tcp/ {++y[$NF]} END {for(w in y) print w, y[w]}'
```
LISTEN 8

ESTABLISHED 2400

FIN_WAIT1 2

TIME_WAIT 6000

 

查看每个ip跟服务器建立的连接数
```sh
netstat -nat|awk '{print$5}'|awk -F : '{print$1}'|sort|uniq -c|sort -rn
```


（PS：正则解析：显示第5列，-F : 以：分割，显示列，sort 排序，uniq -c统计排序过程中的重复行，sort -rn 按纯数字进行逆序排序）

 

查看每个ip建立的ESTABLISHED/TIME_OUT状态的连接数
```sh
netstat -nat|grep ESTABLISHED|awk '{print$5}'|awk -F : '{print$1}'|sort|uniq -c|sort -rn
```
