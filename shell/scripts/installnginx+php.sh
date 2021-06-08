#!/bin/bash
yum install -y epel-release
yum install -y http://rpms.remirepo.net/enterprise/remi-release-7.rpm
yum install -y yum-utils
yum install -y php73-php-fpm php73-php-cli php73-php-bcmath php73-php-gd php73-php-json php73-php-mbstring php73-php-mcrypt php73-php-mysqlnd php73-php-opcache php73-php-pdo php73-php-pecl-crypto php73-php-pecl-mcrypt php73-php-pecl-geoip php73-php-recode php73-php-snmp php73-php-soap php73-php-xmll php73-php-devel php73-php-pear
rpm -ivh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm 
yum install -y nginx

cat >>/etc/profile <EOF
PHP_BIN=/opt/remi/php73/root/usr/bin
export PATH=$PATH:$PHP_BIN
EOF
systemctl enable php73-php-fpm
systemctl start php73-php-fpm
yum install -y php73-php-yaf
cat >/etc/opt/remi/php73/php-fpm.d/www.conf <EOF
[www]
listen = 127.0.0.1:9000
listen.backlog = -1
listen.allowed_clients = 127.0.0.1
listen.owner = www
listen.group = www
listen.mode = 0666
user = www
group = www
pm = dynamic
pm.max_children = 70
pm.start_servers = 50
pm.min_spare_servers = 40
pm.max_spare_servers = 70
pm.max_requests = 2048
pm.process_idle_timeout = 10s
request_terminate_timeout = 300
request_slowlog_timeout = 0
pm.status_path = /php-fpm_status
slowlog = /alidata/logs/php/slow.log
rlimit_files = 51200
rlimit_core = 0
catch_workers_output = yes
;env[HOSTNAME] = office100
env[PATH] = /usr/local/bin:/usr/bin:/bin
env[TMP] = /tmp
env[TMPDIR] = /tmp
env[TEMP] = /tmp
EOF

ln -s /usr/bin/php73 /usr/bin/php
ln -s /opt/remi/php73/root/usr/bin/phpize  /usr/bin/phpize
ln -s /opt/remi/php73/root/usr/bin/php-config  /usr/bin/php-config

systemctl enable nginx
systemctl start nginx 
