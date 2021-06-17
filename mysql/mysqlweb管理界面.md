安装Omnidb
```
wget https://github.com/OmniDB/OmniDB/releases/download/3.0.3b/omnidb-server-3.0.3b_linux_x86_64.rpm
rpm -ivh omnidb-server-3.0.3b_linux_x86_64.rpm
```
nginx反向代理+二次认证
```sh
yum install -y httpd-tools
mkdir -p /usr/local/src/nginx/
htpasswd -c /data/nginx/passwd dieser
```
输入密码


cat /etc/nginx/conf.d/

server {
        listen       80;
        server_name  www.123.com;
        auth_basic "Please input password";
        auth_basic_user_file /data/nginx/passwd;
        location / {
            proxy_pass http://127.0.0.1:8080;
            index  index.html index.htm index.jsp;
        }
    }
