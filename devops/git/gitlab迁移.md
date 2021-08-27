从docker中将gitlab迁移到服务器上。
### innergit
1.进入容器
```sh
docker exec -it 9753e902795a /bin/bash
```
2.备份
```
gitlab-rake gitlab:backup:create
```
3.传输备份文件到新的gitlab服务器
```
scp 1609749148_2021_01_04_13.2.1_gitlab_backup.tar  root@10.0.10.168:~
```
4.传输配置文件到gitlab服务器
```
scp /etc/gitlab/gitlab.rb  root@10.0.10.188:~
```
5.传输secret到gitlab服务器
```
scp /etc/gitlab/gitlab-secrets.json  root@10.0.10.188:~
```
### 新的GItlab服务器
6.下载安装包
```
wget --content-disposition https://packages.gitlab.com/gitlab/gitlab-ce/packages/el/7/gitlab-ce-13.2.1-ce.0.el7.x86_64.rpm/download.rpm
```
7.安装前置软件
```
yum install -y policycoreutils-python
```
8.安装gitlab
```
rpm -ivh gitlab-ce-13.2.1-ce.0.el7.x86_64.rpm 
```
9.将配置文件移到指定位置
```
mv gitlab.rb /etc/gitlab/gitlab.rb
```

10.使配置文件生效，并启动gitlab
```
gitlab-ctl reconfigure
```
11.停止sidekiq服务
```
gitlab-ctl stop sidekiq
```
12.给备份授权
```
chmod 777 1609749148_2021_01_04_13.2.1_gitlab_backup.tar 
```
13.将备份传输到目标目录下
```
mv 1609749148_2021_01_04_13.2.1_gitlab_backup.tar  /var/opt/gitlab/backups/
```
14.进入到目标目录
```
cd /var/opt/gitlab/backups/
```
15.还原备份文件
```
gitlab-rake gitlab:backup:restore BACKUP=1609749148_2021_01_04_13.2.1
```
16 覆盖配置文件gitlab-secrets.json
```
mv gitlab-secrets.json /etc/gitlab/gitlab-secrets.json
```
17.重新启动gitlab
```
gitlab-ctl reconfigure
```
```
gitlab-ctl restart
```
18.浏览器确认
由于gitlab自带的nginx使用的是9002端口，为了方便使用，我们在服务器上安装一个nginx
```sh
sudo rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
```
```sh
sudo yum install -y nginx
```
```sh
sudo systemctl start nginx.service
sudo systemctl enable nginx.service
```
```sh
cat >>/etc/nginx/conf.d/gitlab.conf<<EOF
server {
        listen 80;
        server_name git.dieser.com;
        location / {
            # 设置最大允许上传单个的文件大小
            client_max_body_size 1024m;
            proxy_redirect off;
            #以下确保 gitlab中项目的 url 是域名而不是 http://git，不可缺少
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            # 反向代理到 gitlab 内置的 nginx
            proxy_pass http://127.0.0.1:9002;
            index index.html index.htm;
        }
    }
EOF
```
```sh
nginx -t 
nginx -s reload
```