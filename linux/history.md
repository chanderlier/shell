history 命令显示操作时间、用户和登录IP
```sh
cat >>/etc/bashrc <<"EOF"
HISTFILESIZE=4000       # 默认保存命令是1000条,这里修改为4000条
HISTSIZE=4000
USER_IP=`who -u am i 2>/dev/null| awk '{print $NF}'|sed -e 's/[()]//g'`    # 取得登录客户端的IP
if [ -z $USER_IP ]
then
  USER_IP=`hostname`
fi
HISTTIMEFORMAT="%F %T $USER_IP:`whoami` "    # 设置新的显示history的格式
export HISTTIMEFORMAT
EOF
```
```sh
source /etc/bashrc
```


