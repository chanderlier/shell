## 简介
harbor是一款储存docker镜像的镜像仓库
## 安装
### 安装docker
```bash
yum install -y yum-utils device-mapper-persistent-data lvm2
```
```bash
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```
直接用官方源安装，但可能速度比较慢，可以切换到阿里云、腾讯云、网易云等yum仓库
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
```bash
vim /etc/docker/daemon.json
```

````bash
{
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
### 安装docker-compose
github官方源，国内服务器下载可能很慢
```sh
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
daocloud源下载
```sh
curl -L https://get.daocloud.io/docker/compose/releases/download/1.29.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
```
也可以将docker-compose和harbor等资源放到公司内部的sftp服务器，或者s3、oss等云厂商的储存上。
```sh
chmod +x /usr/local/bin/docker-compose
```
```sh
docker-compose --version
```
安装harbor
下载离线安装包
```sh
tar -zxvf harbor-offline-installer-v2.2.1.tgz
```
```sh
cd harbor
```
```sh
cp harbor.yml.temp harbor.yml
```
### 修改配置文件
#### 修改域名
```sh
hostname: reg.mydomain.com   -> hostname: harbor.dieser.com 修改为指定域名
```
#### 修改端口
```sh
http:
  # port for http, default is 80. If https enabled, this port will redirect to https port
  port: 80 
```
如果没有https的话，需要注释掉对应的https相关内容。
#### 修改admin密码
```sh
harbor_admin_password: Harbor12345 -> harbor_admin_password: YourPASSWD
```
### 安装harbor
```sh
./install.sh
```
### 启动harbor
```sh
docker-compose up -d
```
在本地机器上编辑docker配置文件
```sh
vim /etc/docker/daemon.json
```
```sh
{
"insecure-registries" : ["harbor.dieser.com", "0.0.0.0"]
}
```

### 在本地机器推送镜像到harbor上
```sh
docker tag testimage:v15 harbor.dieser.com/test/testimage:v1
```
```sh
docker push harbor.dieser.com/test/testimage:v1
```