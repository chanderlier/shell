# 通过prometheus、grafana、alertmanager监控
简单介绍如何通过prometheus、grafana、alertmanager实现对服务器性能的监控、可视化、告警等.  
本次测试的服务器为centos7.7  
IP地址：192.168.7.245  
## prometheus
#### 安装prometheus
下载
```sh
wget https://github.com/prometheus/prometheus/releases/download/v2.23.0/prometheus-2.23.0.linux-amd64.tar.gz
```
解压
```sh
tar -zxvf prometheus-2.23.0.linux-amd64.tar.gz 
```
移动到指定目录
```sh
mv prometheus-2.23.0.linux-amd64 /usr/local/bin/prometheus
```
编辑service配置文件
```sh
cat /usr/lib/systemd/system/prometheus.service
```
创建prometheus用户、创建存储数据的文件夹、授权等
```sh
useradd prometheus
```
```sh
mkdir -p /data/prometheus
```
```sh
chown -R prometheus:prometheus /usr/local/bin/prometheus /data/prometheus
```
service配置文件信息如下
```sh
[Unit]
Description= Prometheus
After=network.target

[Service]
Type=simple
User=prometheus
ExecStart=/usr/local/bin/prometheus/prometheus --config.file=/usr/local/bin/prometheus/prometheus.yml --storage.tsdb.path=/data/prometheus/data
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
设置prometheus开机自启动
```sh
systemctl enable prometheus
```
启动prometheus
```sh
systemctl start prometheus
```
check
```
systemctl status prometheus
``` 
web访问 http://192.168.7.245:9090
主要组件
### node_exporter
#### 安装
下载
```sh
wget https://github.com/prometheus/node_exporter/releases/download/v0.21.0/node_exporter-0.21.0.linux-amd64.tar.gz
```
解压
```sh
tar xvf node_exporter-0.21.0.linux-amd64.tar.gz
```
移动到指定目录
```sh
mv node_exporter-0.21.0.linux-amd64 /usr/local/bin/node_exporter
```
编辑service配置文件
```sh
cat /usr/lib/systemd/system/node_exporter.service
```
配置文件信息如下
```sh
[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
ExecStart=/usr/local/bin/node_exporter/node_exporter
Restart=on-failure

[Install]
WantedBy=default.target
```
设置为开机自启动
```sh
systemctl enable node_exporter
```
启动node_exporter
```sh
systemctl start node_exporter
```
check
```sh
systemctl status node_exporter
```
### blackbox_exporter
#### 安装
```sh
wget https://github.com/prometheus/blackbox_exporter/releases/download/v0.18.0/blackbox_exporter-0.18.0.linux-amd64.tar.gz
```
```
tar zxvf blackbox_exporter-0.18.0.linux-amd64
```
```
mv blackbox_exporter-0.18.0.linux-amd64 /usr/local/blackbox_exporter
```
编辑service
```sh
cat /usr/lib/systemd/system/blackbox_exporter
```
service信息如下
```sh
[Unit]
Description=blackbox_exporter
After=network.target

[Service]
User=prometheus
Restart=on-failure
ExecStart=/usr/local/bin/blackbox_exporter/blackbox_exporter  --config.file=/usr/local/bin/blackbox_exporter/blackbox.yml 
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
### mysql_exporter
#### 安装
```
wget https://github.com/prometheus/mysqld_exporter/releases/download/v0.12.1/mysqld_exporter-0.12.1.linux-amd64.tar.gz
```
```
tar zxvf mysqld_exporter-0.12.1.linux-amd64.tar.gz 
```
```
mv mysqld_exporter-0.12.1.linux-amd64 /usr/local/mysql_exporter
```
### consul_exportet
#### 安装
下载
```sh
wget https://github.com/prometheus/consul_exporter/releases/download/v0.7.1/consul_exporter-0.7.1.linux-amd64.tar.gz
```
```
tar -zxvf consul_exporter-0.7.1.linux-amd64.tar.gz
```
```
mv consul_exporter-0.7.1.linux-amd64 /usr/local/consul_exporter
```
## grafana
#### 安装
下载
```sh
wget https://dl.grafana.com/oss/release/grafana-7.3.4-1.x86_64.rpm
```
安装
```sh
yum install -y grafana-7.3.4-1.x86_64.rpm
```
设置为开机自启动
```sh
systemctl enable grafana-server
```
启动grafana
```sh
systemctl start grafana-server
```
check
```sh
systemctl status grafana-server
```
web访问 http://192.168.7.245:3000
username: admin
password: admin
## consul
#### 安装
下载
```sh
yum install -y yum-utils
```
```sh
yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
```
安装
```sh
yum -y install consul
```
启动consul
```
consul agent -dev -client 0.0.0.0 -ui
```
check
```sh
lsof -i:8500
```
另开一个终端
```sh
consul members
```
注册服务
```sh
curl -X PUT -d '{"id": "node-exporter","name": "node-exporter-192.168.7.245","address": "192.168.7.245","port": 9100,"tags": ["test"],"checks": [{"http": "http://192.168.7.245:9100/metrics", "interval": "5s"}]}'  http://192.168.7.245:8500/v1/agent/service/register 
```
在web界面确认  
访问192.168.7.235:8500 确认consul  
访问192.168.7.245:9090 确认prometheus  
注销服务  
```sh
curl -X PUT http://192.168.7.245:8500/v1/agent/service/deregister/node-exporter 
```
坑  
似乎最新的server端已经增加了一段时间不在线即注销对应的服务实例的操作，昨天晚上五点点注册的node-exporter-192.168.7.245，今天早上十点发现consul中已经消失  
## alertmanager
#### 安装
下载
```sh
wget https://github.com/prometheus/alertmanager/releases/download/v0.21.0/alertmanager-0.21.0.linux-386.tar.gz
```
解压
```sh
tar zxvf alertmanager-0.21.0.linux-386.tar.gz
```
移动到指定目录
```sh
mv alertmanager-0.21.0.linux-386.tar.gz /usr/local/alertmanager
```
编辑service配置文件
```sh
cat /usr/lib/systemd/system/alertmanager.service
```
配置文件信息
```sh
[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
ExecStart=/usr/local/node_exporter/node_exporter
Restart=on-failure

[Install]
WantedBy=default.target
```
设置为开机自启动
```sh
systemctl enable alertmanager
```
启动alertmanager
```sh
systemctl start alertmanager
```
check
```
systemctl status alertmanager
```
web访问 http://192.168.7.245:9100