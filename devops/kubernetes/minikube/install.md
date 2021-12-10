安装 docker
```
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

create user minikube
```sh
user add minikube
```
```sh
cat >> /etc/sudoers <<EOF
minikube ALL=(ALL) ALL
minikube ALL=(ALL) NOPASSWD: ALL
EOF
```
grant privilege
```sh
su minikube
```
```sh
sudo usermod -aG docker $USER && newgrp docker
```
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
```
```
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```
```sh
minikube start
```