下载
```sh
wget https://get.helm.sh/helm-v3.5.4-linux-amd64.tar.gz
```
可能下载比较慢，可以使用国内源
```
wget https://mirrors.huaweicloud.com/helm/v3.7.1/helm-v3.7.1-linux-amd64.tar.gz
```
解压
```sh
tar -zxvf helm-v3.5.4linux-amd64.tar.gz
```
移动目录
```sh
mv linux-amd64/helm /usr/local/bin/
```
添加仓库
```sh
helm repo add bitnami https://charts.bitnami.com/bitnami
```