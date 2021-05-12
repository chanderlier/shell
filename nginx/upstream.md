upstream INNER_NGINX_DIESER {
    server 1.2.3.4:30080 weight=1 max_fails=1 fail_timeout=30s;
}
server {
    listen 80;
    server_name www.dieser.com;
    index index.html index.htm index.php;
    autoindex off;
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
        proxy_pass http://INNER_NGINX_DIESER;
        proxy_redirect off;
    }
    access_log  /data/logs/nginx/access/www.dieser.com.log;
    error_log   /data/logs/nginx/error/www.dieser.com.log;
}