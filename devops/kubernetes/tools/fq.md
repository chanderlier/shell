一键脚本
```sh
bash <(curl -sL https://s.hijk.art/xray.sh)
```

手动安装
安装shadowsocks
```sh
pip install shadowsocks
```

添加配置文件
```sh
cat >> /etc/ss.json << EOF
{
  "server": "0.0.0.0",
  "server_port": 10086,
  "local_address": "127.0.0.1",
  "local_port":1080,
  "password": "password",
  "timeout":300,
  "method": "aes-256-cfb",
  "fast_open": false
}
EOF
```
systemd托管
```sh
cat >>/etc/systemd/system/shadowsocks.service << EOF
[Unit]
Description=Shadowsocks
[Service]
TimeoutStartSec=0
ExecStart=/usr/bin/ssserver -c /etc/ss.json
Restart=always
[Install]
WantedBy=multi-user.target
EOF
```
设置开机自启动，启动shadowsocks
```sh
systemctl enable shadowsocks && systemctl start shadowsocks
```