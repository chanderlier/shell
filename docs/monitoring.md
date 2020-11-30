# 通过prometheus、grafana、alertmanager监控
简单介绍如何通过prometheus、grafana、alertmanager实现对服务器性能的监控、可视化、告警等
## prometheus
#### 安装prometheus


主要组件
### node_exporter
#### 安装
```sh
wget https://github.com/prometheus/node_exporter/releases/download/v0.21.0/node_exporter-0.21.0.linux-amd64.tar.gz
```
```sh
tar xvf node_exporter-0.21.0.linux-amd64.tar.gz
```
```sh
mv node_exporter-0.21.0.linux-amd64 /usr/local/node_exporter
```
```sh
cat /usr/lib/systemd/system/node_exporter.service
```
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
### blackbox_exporter
#### 安装
wget
### mysql_exporter
#### 安装
wget
### consul
#### 安装
wget 
## grafana
#### 安装
w
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