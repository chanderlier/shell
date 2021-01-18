给指定的文件类型批量改名,比如添加时间。
一般用在给文件备份的时候，加上时间，便于区别。
举例
现在有a.txt b.txt ..... m.txt若干个文件
现在统一需要将它们改成a-20201027.txt形式
创建txt文件
```bash
touch {a..m}.txt
```
```bash
ls
```
```bash
[root@s-01 111]# ls
a.txt  b.txt  c.txt  d.txt  e.txt  f.txt  g.txt  h.txt  i.txt  j.txt  k.txt  l.txt  m.txt
```

```bash
vim addtime.sh
```
```bash
#!/bin/bash
datetime=`date "+%Y%m%d-%H%M%S"` #%Y%m%d代表年月日，%H%M%S代表时分秒。如果一天只备份一次的话，可以不需要时分秒这个参数。
for file in `ls |grep .txt`#ls |grep .txt 列出并筛选带.txt的文件，for file in `ls |grep .txt`则是对目标文件进行for循环
do
  newfile=`echo $file |sed  's/.txt/'-$datetime'&/'`#在.txt前添加-$datetime，实际效果就是-20201027.txt
  mv $file $newfile #文件改名
done
```

```sh
[root@s-01 111]# sh addtime.sh
```
```sh
[root@s-01 111]# ls
a-20201027-210721.txt  b-20201027-210721.txt  d-20201027-210721.txt  f-20201027-210721.txt  h-20201027-210721.txt  j-20201027-210721.txt  l-20201027-210721.txt
addtime.sh             c-20201027-210721.txt  e-20201027-210721.txt  g-20201027-210721.txt  i-20201027-210721.txt  k-20201027-210721.txt  m-20201027-210721.txt
```