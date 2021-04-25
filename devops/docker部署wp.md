首先准备一台云服务器、弹性公网IP、域名。做好VPC设置，确保通过域名可以正常访问你的服务器。

| 云服务商 | 系统               | 域名         | IP         | VPC              |
| -------- | ------------------ | ------------ | ---------- | ---------------- |
| aws      | Amazon Linux 2 AMI | my.dieser.cn | 弹性公网IP | 端口、IP访问设置 |
|          |                    |              |            |                  |

安装docker

安装docker
```bash
amazon-linux-extras intall -y docker
```
如果是centos7或者centos8的话，可以用以下方式安装docker
```bash
yum install -y yum-utils device-mapper-persistent-data lvm2
```
```bash
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```
```bash
yum install -y docker-ce
```
设置docker开机自启动
```bash
systemctl enable docker 
```
启动docker
```bash
systemctl start docker
```

使用镜像加速器

阿里云镜像获取地址：https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors，登陆后，左侧菜单选中镜像加速器就可以看到你的专属地址了：

![image-20201025220408157](C:\Users\refrain\AppData\Roaming\Typora\typora-user-images\image-20201025220408157.png)

```bash
vim /etc/docker/daemon.json
```

````bash
{
  "registry-mirrors": ["https://12345678.mirror.aliyuncs.com"],
  "registry-mirrors": ["https://4wgtxa6q.mirror.aliyuncs.com"]
}
````
重新载入配置文件
```bash
systemctl daemon-reload
```
重启docker，使配置生效
````bash
systemctl restart docker 
````

wordpress安装
拉取wordpress最新版的镜像文件
```bash
docker pull wordpress:latest
```
拉取mysql:5.7的镜像文件
```bash
docker pull mysql:5.7
```
docker运行mysql
```bash
docker run -d --privileged=true --name mysql -v /data/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -p 23306:3306 mysql:5.7
```
docker运行wordpress
```bash
docker run -d --name wordpress -e WORDPRESS_DB_HOST=mysql -e WORDPRESS_DB_USER=root -e WORDPRESS_DB_PASSWORD=123456 -e WORDPRESS_DB_NAME=wordpress -p 1080:80 --link mysql:mysql wordpress
```
查看容器是否正常运行
```bash
docker ps 
```
设置mysql自动重启
```bash
docker update mysql --restart=always
```
设置wordpress自动启动
```bash
docker update wordpress --restart=always
```

浏览器访问 http://my.dieser.cn:1080,进入后续设置。
