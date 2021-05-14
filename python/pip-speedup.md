单个模块加速
```sh
pip install module -i https://pypi.tuna.tsinghua.edu.cn/simple
```
永久
```sh
mkdir ~/.pip
```
```sh
vim ~/.pip/pip.conf
```
```sh
 [global]
 index-url = https://pypi.tuna.tsinghua.edu.cn/simple
 ```