pip设置默认使用国内镜像源 
```sh
mkdir ~/.pip
```
```sh
cat ~/.pip/pip.conf
```
```sh
## Note, this file is written by cloud-init on first boot of an instance
## modifications made here will not survive a re-bundle.
###
[global]
index-url=http://mirrors.cloud.aliyuncs.com/pypi/simple/

[install]
trusted-host=mirrors.cloud.aliyuncs.com
```
暂时使用
```sh
pip3 install -r requirement -i http://mirrors.cloud.aliyuncs.com/pypi/simple/
```
```sh
pip3 install mysqlclient -i http://mirrors.cloud.aliyuncs.com/pypi/simple/
```