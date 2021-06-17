#!/bin/bash
### 安装proxychains4
git clone https://github.com/rofl0r/proxychains-ng.git
cd proxychains-ng
./configure
make && sudo make install
cp ./src/proxychains.conf /etc/proxychains.conf

### 安装shadowsocks
```sh
pip install shadowsocks
```

```sh
cat >>/etc/ss.json <EOF
{
  "server":"ip",
  "local_address":"127.0.0.1",
  "local_port":1086,
  "server_port":10240,
  "password":"passwd",
  "timeout":300,
  "method":"aes-256-cfb"
}
EOF
```

```sh
nohup sslocal -c /etc/ss.json >/dev/null 2>&1
```

```sh
proxychains curl cip.cc
```