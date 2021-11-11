package main

import (
	"fmt"
	"log"

	"github.com/go-redis/redis"
)

var rdb *redis.Client

func main() {
	rdb = redis.NewClient(&redis.Options{
		Addr:     "公网访问链接地址.redis.rds.aliyuncs.com:6379",
		Password: "自定义用户名:密码",
		DB:       0,
	})
	_, err := rdb.Ping().Result()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("连接成功")
}
