下载
```sh
wget https://get.helm.sh/helm-v3.5.4-linux-amd64.tar.gz
```
解压
```sh
tar -zxvf helm-v3.5.4linux-amd64.tar.gz
```
移动目录
```sh
mv linux-amd64/helm /usr/local/bin/helm
```
初始化
```sh
helm init --upgrade -i registry.cn-hangzhou.aliyuncs.com/google_containers/tiller:v3.5.4  --stable-repo-url https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
```