现有一个php项目，前后端分离，需要从服务器迁移到aks上。
### 前端
#### 创建前端目录 
```sh
mkdir frontend
```
#### 编写前端服务器Dockerfile
```sh
cat Dockerfile
```
```Dockerfile
From centos:centos7.7.1904
ARG workdir=/data/www/test.dieser.com
WORKDIR ${workdir}
RUN rpm -ivh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm 
RUN yum update -y \
    && yum install -y epel-release \
    nginx

RUN mkdir -p /data/logs/nginx

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/conf.d/vhosts/test.dieser.com.conf /etc/nginx/conf.d/vhosts/test.dieser.com.conf
COPY src /alidata/www/test.dieser.com/

RUN rm -rf /etc/nginx/conf.d/default.conf
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/shanghai" > /etc/timezone
RUN useradd -M -s /sbin/nologin www && chown -R www:www /data 

COPY start.sh /etc/start.sh
RUN chmod 755 /etc/start.sh
ENTRYPOINT ["/etc/start.sh"]
```
#### 创建目录并编写k8s文件
```sh
mkdir k8s
```
```sh
cat k8s/deploy.yaml
```
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: dieser
  namespace: dieser
spec:
  selector:
    matchLabels:
      app: dieser
  replicas: 1
  template:
    metadata:
      labels:
        app: dieser
    spec:
      containers:
      - name: dieser
        image: frontend:v1
        env:
        - name: POD_NAME
          valueFrom:
            fieldRef:
              apiVersion: v1
              fieldPath: metadata.name
        ports:
        - containerPort: 80
          protocol: TCP
        resources:
          requests:
            cpu: 1000m
            memory: 2048Mi
          limits:
            cpu: 1000m
            memory: 2048Mi
```
```sh
cat k8s/service
```
```yaml
apiVersion: v1
kind: Service
metadata:
  name: dieser-service
  namespace: dieser
  annotations:
    service.beta.kubernetes.io/azure-load-balancer-internal: "true"
spec:
  type: LoadBalancer 
  loadBalancerIP: 10.1.101.5
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: dieser    
```
#### 创建nginx目录及配置文件
```sh
mkdir -p nginx/conf.d/vhosts
```
```sh
cat nginx/nginx.conf
```
```sh
user  www;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/conf.d/vhosts/*.conf;
}
```
```sh
cat nginx/conf.d/vhosts/test.dieser.com.conf
```
```sh
server {
    listen 80;
    server_name 10.1.101.5;
    index index.html index.htm;
    root /data/www/test.dieser.com;
    location / {
         try_files $uri $uri/ /index.html;
    }
    location /api/ {
        proxy_pass http://10.1.101.6:80/;
        proxy_redirect     off;
        proxy_set_header   Host             $host;
        proxy_set_header   X-Real-IP        $remote_addr;
        proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
    }
    access_log  /data/logs/nginx/test.dieser.com.log;
    error_log /data/logs/nginx/test.dieser.com-error.log;
}
```
####  创建源码目录src
```sh
mkdir src
```
上传代码到src目录下
#### 创建docker image
```sh
docker build -t frontend:v1 .
```
### 构建cicd流程
