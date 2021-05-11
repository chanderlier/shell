centos7
```sh
yum install ansible -y
```
macos 
```sh
pip3 install ansible
```
如果涉及到密码认证那块，需要安装sshpass模块
```sh
ansible-playbook -i hosts main.yml
```
提示{to use the 'ssh' connection type with passwords, you must install the sshpass program"}
我们需要安装sshpass
参考homebrew/config.md，替换homebrew的仓库源，然后执行下面的命令
```sh
wget https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb
```
```sh
brew install sshpass
```