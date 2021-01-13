#!/bin/bash
set -xeu
green_echo ()  { echo -e  "\033[032;1m $@ \033[0m"; }
prefix=${1/-/_}
db_name=${prefix}db
user=${prefix}user
passwd=$(date +%s |sha256sum |base64 |head -c 16)
conn_db_cmd="/usr/bin/mysql -uroot -p'123456' -h127.0.0.1"
create_db="CREATE DATABASE IF NOT EXISTS  ${db_name} DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"
remote_ip=( '172.16.%'  '192.168.%' '10.0.%' )
# create db
eval ${conn_db_cmd} -e \"${create_db}\"
for ip in ${remote_ip[@]}; do
    # create user and add privileges
    green_echo ${conn_db_cmd} -e \"GRANT ALL PRIVILEGES ON ${db_name}.* TO ${user}@\'${ip}\' IDENTIFIED BY \'${passwd}\'\"
    eval ${conn_db_cmd} -e \"GRANT ALL PRIVILEGES ON ${db_name}.* TO ${user}@\'${ip}\' IDENTIFIED BY \'${passwd}\'\"
done
# flush privileges
eval ${conn_db_cmd} -e \"flush privileges\"
echo 
echo
green_echo "db_name: ${db_name} user: ${user} passwd: ${passwd}"
