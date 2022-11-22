#!/bin/bash
APP_NAME=app-name
APP_PATH=/path

usage() {
    echo "Usage: sh script.sh [start|stop|restart|status]"
    exit 1
}

is_exist() {
    pid=`ps -ef|grep $APP_NAME|grep -v grep|awk '{print $2}'`
    if [ -z "${pid}" ]; then
    return 1
    else
    return 0
    fi
}

build() {
    cd $APP_PATH && go build
    echo "go build $APP_NAME"
}

start() {
    is_exist
    if [ $? -eq "0" ]; then
    echo "${APP_NAME} is already running. pid=${pid} ."
    else
     cd $APP_PATH && nohup ./$app-name > log.txt 2>&1 &
    echo "${APP_NAME} start success"
    fi
}

stop() {
    is_exist
    if [ $? -eq "0" ];then
    kill -9 $pid
    else
    echo "${APP_NAME} is not running."
    fi
}

restart() {
    build
    stop
    start
}

case "$1" in
 "start")
 start
 ;;
 "stop")
 stop
 ;;
 "restart")
 restart;;
 *)
 usage
 ;;
esac


```sh
/usr/bin/ssh www@ts-web-dev /usr/bin/bash /alidata/www/scripts/restart.sh restart >/dev/null 2>&1 &
```