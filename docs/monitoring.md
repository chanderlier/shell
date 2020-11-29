# 通过prometheus、grafana、alertmanager监控
简单介绍如何通过prometheus、grafana、alertmanager实现对服务器性能昨天的监控、可视化、告警等
## prometheus
#### 安装prometheus


主要组件
### node_exporter
#### 安装
### blackbox_exporter
#### 安装
### mysql_exporter
#### 安装
### consul
#### 安装
## grafana
#### 安装
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