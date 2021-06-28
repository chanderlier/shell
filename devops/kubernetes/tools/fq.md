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



```bash
yum install -y yum-utils device-mapper-persistent-data lvm2
```
```bash
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```
```bash
yum install -y docker-ce
```
设置docker开机自启动
```bash
systemctl enable docker 
```
启动docker
```bash
systemctl start docker
```
```sh
yum install -y certbot
certbot certonly --standalone
输入自己的域名
```
```sh
cat >> proxy.sh <<EOF
#!/bin/bash
## 下面的四个参数需要改成你的
DOMAIN="YOU.DOMAIN.NAME"
USER="username"
PASS="password"
PORT=443

BIND_IP=0.0.0.0
CERT_DIR=/etc/letsencrypt
CERT=${CERT_DIR}/live/${DOMAIN}/fullchain.pem
KEY=${CERT_DIR}/live/${DOMAIN}/privkey.pem
sudo docker run -d --name gost \
    -v ${CERT_DIR}:${CERT_DIR}:ro \
    --net=host ginuerzh/gost \
    -L "http2://${USER}:${PASS}@${BIND_IP}:${PORT}?cert=${CERT}&key=${KEY}&probe_resist=code:404&knock=www.google.com"
EOF
```
验证
```sh
curl -v "https://www.google.com" --proxy "https://DOMAIN" --proxy-user 'USER:PASS'
```

添加crontab
```sh
crontab -e
```
```sh
0 0 1 * * /usr/bin/certbot renew --force-renewal
5 0 1 * * /usr/bin/docker restart gost
```


客户端 
```sh
gost -L ss://aes-256-cfb:passcode@:1080 -F 'https://USER:PASS@DOMAIN:443'
```