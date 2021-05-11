官网建议macos安装ansible的方式是通过pip安装。homebrew安装也行
```sh
pip3 install ansible
```
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
最后
```sh
ansible-playbook -i hosts main.yml
```