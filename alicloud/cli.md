download aliyun cli 
```sh
wget https://github.com/aliyun/aliyun-cli/releases/download/v3.0.62/aliyun-cli-linux-3.0.62-amd64.tgz
```
解压
```sh
tartar xzvf aliyun-cli-linux-3.0.62-amd64.tgz
```
执行如下命令，将aliyun程序移动到到/usr/local/bin目录中。
```sh
mv aliyun /usr/local/bin
```



init
```sh
aliyun configure
aliyun Access Key ID [None]: xxxxx
aliyun Access Key Secret [None]: xxxxx
Default Region Id [None]: cn-hangzhou # 地域ID
Default Output Format [json]: json (Only supports JSON) # 目前仅支持JSON
Default Language [zh|en]: en # 在这里选择英语
```
获取本地实例信息
```sh
aliyun ecs DescribeInstances --output cols=InstanceId,InstanceName rows=Instances.Instance[]
```

```sh
InstanceId             | InstanceName
----------             | ------------
i-uf6hf4qqoc03n42juo3j | master
i-uf68987vinv7y5m4d49b | dieser-s
```