```sh
cat es.go
```
```go
package main

import (
    "github.com/elastic/go-elasticsearch"
    "log"
)

// es操作

// 创建客户端
func main() {
    // 连接es

    // elasticsearch.Config 配置ES连接属性
    /*
        type Config struct {
                Addresses []string // 要使用的Elasticsearch节点列表.
                Username  string   // HTTP基本身份验证的用户名.
                Password  string   // HTTP基本认证密码.

                CloudID string // 弹性服务的端点 (https://elastic.co/cloud).
                APIKey  string // 用于授权的Base64编码令牌；如果设置，则覆盖用户名和密码.

                RetryOnStatus        []int // 重试状态代码列表. 默认: 502, 503, 504.
                DisableRetry         bool  // 默认: false.
                EnableRetryOnTimeout bool  // 默认: false.
                MaxRetries           int   // 默认: 3.

                DiscoverNodesOnStart  bool          // 初始化客户端时发现节点. Default: false.
                DiscoverNodesInterval time.Duration // 定期发现节点. Default: disabled.

                EnableMetrics     bool // 启用指标收集.
                EnableDebugLogger bool // 启用调试日志记录.

                RetryBackoff func(attempt int) time.Duration // 可选的退避时间. 默认: nil.

                Transport http.RoundTripper    // HTTP传输对象.
                Logger    estransport.Logger   // 记录器对象.
                Selector  estransport.Selector // 选择器对象.

                // 自定义ConnectionPool的可选构造函数. Default: nil.
                ConnectionPoolFunc func([]*estransport.Connection, estransport.Selector) estransport.ConnectionPool
            }
    */
    cfg := elasticsearch.Config{
        Addresses: []string{
            "http://10.0.10.168:9200",
        },
        // ...
    }

    es, err := elasticsearch.NewClient(cfg)
    if err != nil {
        log.Fatalf("Error creating the client: %s", err)
    }
    // 获取 当前es的详细信息
    res, err := es.Info()
    if err != nil {
        log.Fatalf("Error getting response: %s", err)
    }
    defer res.Body.Close()
    log.Printf("%#v\n", res)
    log.Printf("%v\n", res)
}
```
初始化
```sh
go mod init es.go
```
安装es插件
```sh
go get github.com/elastic/go-elasticsearch
```
测试连接情况
```sh
go run es.go
```