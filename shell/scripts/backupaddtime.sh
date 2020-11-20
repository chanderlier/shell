#!/bin/bash
datetime=`date "+%Y%m%d-%H%M%S"` #%Y%m%d代表年月日，%H%M%S代表时分秒。如果一天只备份一次的话，可以不需要时分秒这个参数。
for file in `ls |grep .txt`#ls |grep .txt 列出并筛选带.txt的文件，for file in `ls |grep .txt`则是对目标文件进行for循环
do
  newfile=`echo $file |sed  's/.txt/'-$datetime'&/'`#在.txt前添加-$datetime，实际效果就是-20201027.txt
  mv $file $newfile #文件改名
done