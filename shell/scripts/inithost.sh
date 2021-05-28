#/bin/bash
<<!
 **********************************************************
 * Author        : dieser
 * Email         : dieser@163.com
 * Last modified : 2020-12-22 14:34
 * Filename      : init.sh
 * Description   : 
 * *******************************************************
!

egrep "^ops" /etc/passwd >& /dev/null  
if [ $? -ne 0 ]  
then  
    useradd  ops 
fi  

su - ops <<EOF
cd ~;
mkdir .ssh;
chmod 700 .ssh;
echo "ssh-rsa id_rsa.pub dieser@163.com"    >> .ssh/authorized_keys;                               
"    >> .ssh/authorized_keys;                               

chmod 600 .ssh/authorized_keys;
EOF
echo "ops用户已创建"

egrep "^dev" /etc/passwd >& /dev/null  
if [ $? -ne 0 ]  
then  
    useradd  dev  
fi  

su - dev <<EOF
cd ~;
mkdir .ssh;
chmod 700 .ssh;
echo "id_rsa.pub" >> .ssh/authorized_keys;
chmod 600 .ssh/authorized_keys;
EOF

echo "dev用户已创建"
cat >> /etc/sudoers <<EOF
ops    ALL=(ALL)      NOPASSWD: ALL
EOF
echo "赋予ops用户sudo权限"
#  禁止用户采用密码登录
sed -i -e 's/#AuthorizedKeysFile/AuthorizedKeysFile/g' /etc/ssh/sshd_config
sed -i -e 's/PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/sshd_config
echo "已禁止用户通过密码登录"
sed -i -e 's/#PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config
echo "已禁止root用户登录"
#  重启sshd
systemctl restart sshd
