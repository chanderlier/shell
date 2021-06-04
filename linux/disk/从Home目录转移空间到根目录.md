一开始创建centos时给/home分配了空间，现在需要将/home目录下的空间转移到根目录
创建备份文件夹
```sh
mkdir /backup  
```
```sh
mv /home/* /backup/  
```
卸载/home
```sh
umount /home  
```
移除lv
```sh
lvremove /dev/centos/home  
```
```sh
lvdisplay
```
```sh
lvextend -L +49G /dev/centos/root  
```
查看磁盘文件系统格式
```
df -T
```
扩容
```sh
xfs_growfs /dev/centos/root  
```
```sh
mv /backup/* /home/  
```
```
rm -rf /backup  
```