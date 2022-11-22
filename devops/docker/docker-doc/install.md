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
```bash
systemctl restart docker 
```
docker-compose
```sh
```