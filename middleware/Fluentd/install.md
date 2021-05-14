```sh
ulimit -n
```
```sh
cat >>etc/security/limits.conf<<EOF
root soft nofile 65536
root hard nofile 65536
* soft nofile 65536
* hard nofile 65536
EOF
```
```sh
cat >>/etc/sysctl.conf<<EOF
net.core.somaxconn = 1024
net.core.netdev_max_backlog = 5000
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.ipv4.tcp_wmem = 4096 12582912 16777216
net.ipv4.tcp_rmem = 4096 12582912 16777216
net.ipv4.tcp_max_syn_backlog = 8096
net.ipv4.tcp_slow_start_after_idle = 0
net.ipv4.tcp_tw_reuse = 1
net.ipv4.ip_local_port_range = 10240 65535
```
```sh
sysctl -p
```
```sh
curl -L https://toolbelt.treasuredata.com/sh/install-redhat-td-agent4.sh | sh
```