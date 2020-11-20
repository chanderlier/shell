find / -mtime 0 //24小时内更改过内容的文件列出
find / -mtime -5 //五天之内被更改过的文件名
find / -mtime +5 //五天之前被更改过的文件名，大于等于六天前的文件名
find / -mtime 5  //5-6那一天的档案名
find /var/log -type f -mtime +7 -ok rm {} \;  //查找/var/log目录中更改时间在7日以前的普通文件，并在删除之前询问它们：
find . -type f -perm 644 -exec ls -l {} \;  //查找前目录中文件属主具有读、写权限，并且文件所属组的用户和其他用户具有读权限的文件：
find / -type f -size 0 -exec ls -l {} \;    //为了查找系统中所有文件长度为0的普通文件，并列出它们的完整路径：
find . -type f -name *.bk -mtime +7 -exec rm {} \ //找出当前目录下文件后缀为.bk,七天之前的文件，并删除





