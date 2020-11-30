# 通过prometheus、grafana、alertmanager监控
简单介绍如何通过prometheus、grafana、alertmanager实现对服务器性能的监控、可视化、告警等
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
mv prometheus-2.23.0.linux-amd64 /usr/local/prometheus
```
编辑service配置文件
```sh
cat /usr/lib/systemd/system/prometheus.service
```
service配置文件信息如下
```sh
[Unit]
Description=Prometheus Server
Documentation=https://prometheus.io/docs/introduction/overview/
After=network-online.target

[Service]
User=prometheus
Restart=on-failure
ExecStart=/usr/local/prometheus/prometheus \
  --config.file=/usr/local/prometheus/prometheus.yml \
  --storage.tsdb.retention=30d \
  --storage.tsdb.path=/data/prometheus/data
ExecReload=/bin/kill -HUP $MAINPID
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
mv node_exporter-0.21.0.linux-amd64 /usr/local/node_exporter
```
编辑service配置文件
```sh
cat /usr/lib/systemd/system/node_exporter.service
```
配置文件信息如下
```sh
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
wget https://github.com/prometheus/blackbox_exporter/releases/download/v0.18.0/blackbox_exporter-0.18.0.linux-amd64.tar.gz
### mysql_exporter
#### 安装
wget https://github.com/prometheus/mysqld_exporter/releases/download/v0.12.1/mysqld_exporter-0.12.1.linux-amd64.tar.gz
### consul
#### 安装
下载
```sh
wget https://github.com/prometheus/consul_exporter/releases/download/v0.7.1/consul_exporter-0.7.1.linux-amd64.tar.gz
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