```sh
[root@gitlab ~]# fdisk /dev/vdb
欢迎使用 fdisk (util-linux 2.23.2)。

更改将停留在内存中，直到您决定将更改写入磁盘。
使用写入命令前请三思。

Device does not contain a recognized partition table
使用磁盘标识符 0xd3ed5605 创建新的 DOS 磁盘标签。

命令(输入 m 获取帮助)：
命令(输入 m 获取帮助)：n
Partition type:
   p   primary (0 primary, 0 extended, 4 free)
   e   extended
Select (default p): p
分区号 (1-4，默认 1)：1
起始 扇区 (2048-209715199，默认为 2048)：
将使用默认值 2048
Last 扇区, +扇区 or +size{K,M,G} (2048-209715199，默认为 209715199)：
将使用默认值 209715199
分区 1 已设置为 Linux 类型，大小设为 100 GiB

命令(输入 m 获取帮助)：w
The partition table has been altered!

Calling ioctl() to re-read partition table.
正在同步磁盘。
```
格式化磁盘
```sh
mkfs.etx4 /dev/vdb1
```
查看磁盘uuid
```sh
blkid
```
新建目录
```sh
mkdir /data
```
写入开机启动
```sh
echo "UUID=xxxx  /data ext4 defaults 0 0 " >> /etc/fstab
```
挂载
```sh
mount -a 
```