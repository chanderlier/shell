nginx
默认未安装
安装
```bash
yum install -y nginx
```
设置为开机自启动
```bash
systemctl enable nginx
```
启动nginx
```bash
nginx -c /etc/nginx/nginx.conf
```
常见指令
```bash
nginx -s reload  # 向主进程发送信号，重新加载配置文件，热重启
nginx -s reopen	 # 重启 Nginx
nginx -s stop    # 快速关闭
nginx -s quit    # 等待工作进程处理完成后关闭
nginx -T         # 查看当前 Nginx 最终的配置
nginx -t -c <配置路径>    # 检查配置是否有问题，如果已经在配置目录，则不需要-c
```
修改配置文件
/etc/nginx/conf.d/ 文件夹，是我们进行子配置的配置项存放
／etc/nginx/nginx.conf 是我们的主配置文件

```bash
main        # 全局配置，对全局生效
├── events  # 配置影响 Nginx 服务器或与用户的网络连接
├── http    # 配置代理，缓存，日志定义等绝大多数功能和第三方模块的配置
│   ├── upstream # 配置后端服务器具体地址，负载均衡配置不可或缺的部分
│   ├── server   # 配置虚拟主机的相关参数，一个 http 块中可以有多个 server 块
│   ├── server
│   │   ├── location  # server 块可以包含多个 location 块，location 指令用于匹配 uri
│   │   ├── location
│   │   └── ...
│   └── ...
└── ...
```

```bash
user  nginx;                        # 运行用户，默认即是nginx，可以不进行设置,如果和php一起使用，按需要改成www之类的
worker_processes  1;                # Nginx 进程数，一般设置为和 CPU 核数一样
error_log  /var/log/nginx/error.log warn;   # Nginx 的错误日志存放目录,可以指定为其他目录
pid        /var/run/nginx.pid;      # Nginx 服务启动时的 pid 存放位置

events {
    use epoll;     # 使用epoll的I/O模型(如果你不知道Nginx该使用哪种轮询方法，会自动选择一个最适合你操作系统的)
    worker_connections 1024;   # 每个进程允许最大并发数
}

http {   # 配置使用最频繁的部分，代理、缓存、日志定义等绝大多数功能和第三方模块的配置都在这里设置
    # 设置日志模式
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;   # Nginx访问日志存放位置

    sendfile            on;   # 开启高效传输模式
    tcp_nopush          on;   # 减少网络报文段的数量
    tcp_nodelay         on;
    keepalive_timeout   65;   # 保持连接的时间，也叫超时时间，单位秒
    types_hash_max_size 2048;

    include             /etc/nginx/mime.types;      # 文件扩展名与类型映射表
    default_type        application/octet-stream;   # 默认文件类型

    include /etc/nginx/conf.d/*.conf;   # 加载子配置项
    include /etc/nginx/conf.d/vhost/*.conf #加载子配置项#
    server {
    	listen       80;       # 配置监听的端口
    	server_name  localhost;    # 配置的域名
    	
    	location / {
    		root   /usr/share/nginx/html;  # 网站根目录
    		index  index.html index.htm;   # 默认首页文件
    		deny 192.168.0.3;   # 禁止访问的ip地址，可以为all,可以理解为IP黑名单
    		allow 192.168.0.2；# 允许访问的ip地址，可以为all
    	}
    	
    	error_page 500 502 503 504 /50x.html;  # 默认50x对应的访问页面
    	error_page 400 404 error.html;   # 同上
    }
}
```

反向代理
```bash
server {
  listen 9001;
  server_name *.dieser.cn;

  location ~ /test/ {
    proxy_pass http://127.0.0.1:8080;
  }
  
  location ~ /study/ {
    proxy_pass http://127.0.0.1:8081;
  }
}
```



跨域 
比如前端站点是 b.dieser.cn，这个地址下的前端页面请求 a.dieser.cn 下的资源，
```bash
cat  /etc/nginx/conf.d/a.dieser.cn.conf
```
```bash
server {
  listen       80;
  server_name  a.dieser.cn;
  
	add_header 'Access-Control-Allow-Origin' $http_origin;   # 全局变量获得当前请求origin，带cookie的请求不支持*
	add_header 'Access-Control-Allow-Credentials' 'true';    # 为 true 可带上 cookie
	add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';  # 允许请求方法
	add_header 'Access-Control-Allow-Headers' $http_access_control_request_headers;  # 允许请求的 header，可以为 *
	add_header 'Access-Control-Expose-Headers' 'Content-Length,Content-Range';
	
  if ($request_method = 'OPTIONS') {
		add_header 'Access-Control-Max-Age' 1728000;   # OPTIONS 请求的有效期，在有效期内不用发出另一条预检请求
		add_header 'Content-Type' 'text/plain; charset=utf-8';
		add_header 'Content-Length' 0;
    
		return 204;                  # 200 也可以
	}
  
	location / {
		root  /usr/share/nginx/html/be;
		index index.html;
	}
}
```

负载均衡
```bash
http {
  upstream myserver {
  	# ip_hash;  # ip_hash 方式
    # fair;   # fair 方式
    server 127.0.0.1:8080 weight=1; # 负载均衡目的服务地址
    server 127.0.0.1:8081 weight=5;
    server 127.0.0.1:8082 weight=10;  # weight 方式，不写默认为 1
  }
 
  server {
    location / {
    	proxy_pass http://myserver;
      proxy_connect_timeout 10;
    }
  }
}
```
过滤
```bash
# 非指定请求全返回 403
if ( $request_method !~ ^(GET|POST|HEAD)$ ) {
  return 403;
}

location / {
  allow 192.168.0.2;  
  deny all;  #IP访问限制（只允许IP是 192.168.0.2 机器访问）
  
  root   html;
  index  index.html index.htm;
}
```

图片缓存
```bash
# 图片缓存时间设置
location ~ .*\.(gif|jpg|png|htm|html|css|js)$ {
	expires 10d;
}

# 如果不希望缓存
expires -1;
```
举例
```bash
proxy_cache_path /tmp/nginx_proxy_cache levels=1 keys_zone=cache_one:512m inactive=60s max_size=1000m;  

# server 区域下添加缓存配置 
location ~ \.(gif|jpg|png|htm|html|css|js)(.*) {  
    proxy_pass http://192.168.0.2:5000；#如果没有缓存则转向请求 
    proxy_redirect off;   
    proxy_cache cache_one;   
    proxy_cache_valid 200 1h;            #对不同的 HTTP 状态码设置不同的缓存时间  
    proxy_cache_valid 500 1d; 
    proxy_cache_valid any 1m;  
    expires 3d; 
} 
```

动静分离
```bash
upstream static {   
    server 192.167.2.91:80; 
}  

upstream dynamic {     
    server 192.167.2.92:8080; 
}  

server { 
    listen       80;   #监听端口  
    server_name  www.dieser.cn; 监听地址 

    # 拦截动态资源  
    location ~ .*\.(php|jsp)$ {  
        proxy_pass http://dynamic;
    }   
      
    # 拦截静态资源 
    location ~ .*\.(jpg|png|htm|html|css|js)$ {  
        root /data/;  #html目录 
        proxy_pass http://static;    
        autoindex on;;  #自动打开文件列表  
    }
} 
```