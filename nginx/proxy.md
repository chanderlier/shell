现在有个需求，前后端服务器都只开放了80 443端口，但后端服务器80端口只有前端服务器能访问。客户端在只能访问前端服务器的环境下，没有https，如何访问后端服务器。  
前端服务器 IP 10.0.10.1  
后端服务器 IP 10.0.10.2   

前端服务器 nginx.conf
```sh
server {
    listen 80;
    server_name 10.0.10.1;
    index index.html index.htm;
    root /data/www/test.dieser.com;
    location / {
         try_files $uri $uri/ /index.html;
    }
    location /api/ {
        proxy_pass http://10.0.10.2:80/;
        proxy_redirect     off;
        proxy_set_header   Host             $host;
        proxy_set_header   X-Real-IP        $remote_addr;
        proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
    }
    access_log  /data/logs/nginx/test.dieser.com.log;
    error_log /data/logs/nginx/test.dieser.com-error.log;
}
```