通过slb加nginx，实现通过域名访问到内网接口
域名解析
将域名解析到slb
slb对应的服务器上新增nginx.conf
```
server {
    listen 80;
    server_name for.example.com
    location / {
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_set_header X-NginX-Proxy true;
        client_max_body_size 10m;
        client_body_buffer_size 128k;
        proxy_connect_timeout 120;
        proxy_send_timeout 120;
        proxy_read_timeout 120;
        # proxy_timeout  10m; #默认值为10分钟，nginx接收后端服务器的响应超时时间
        proxy_pass http://外网ip:port;
        proxy_redirect off;
    }
    access_log  /alidata/logs/nginx/access/forexample.log;
    error_log   /alidata/logs/nginx/forexample-error.log;
```
路由器上设置nat
内网ip：port -> 外网ip：port
