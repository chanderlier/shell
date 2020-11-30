# 通过prometheus、grafana、alertmanager监控
简单介绍如何通过prometheus、grafana、alertmanager实现对服务器性能的监控、可视化、告警等
## prometheus
#### 安装prometheus


主要组件
### node_exporter
#### 安装
wget
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
```sh
wget https://github.com/prometheus/alertmanager/releases/download/v0.21.0/alertmanager-0.21.0.linux-386.tar.gz
```
```sh
tar zxvf alertmanager-0.21.0.linux-386.tar.gz
```
```sh
mv alertmanager-0.21.0.linux-386.tar.gz /usr/local/alertmanager
```
```sh
cat /usr/lib/systemd/system/alertmanager.service
```