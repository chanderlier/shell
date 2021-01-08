目前主要用到的aliyun的服务
ECS、OSS、RDS、RAM、VPC、SLB、ACK、ACS、ACR、域名解析、域名备案、OOS、CDN等
管理工具：jumpserver、ansible、terraform、oos、python+aliyun sdk
运维工具：ansible、terraform、oos
jumpserver：管理登录服务器的用户、通过自带的ansible管理服务器内部资源
ansible：管理服务器内部资源，比如修改hosts，resolv.conf，批量部署管理应用等
terraform：管理阿里云服务，比如开通ecs，开通oss bucket accesskey等
python+aliyun sdk：批量将公网IP转换为EIP，批量添加CDN
oos：批量更换弹性ip，定时运维，批量向目标服务器下达命令等。
ECS：云服务器
    - 创建
        - 控制台
        - acsclient
        - terraform
    - 磁盘扩容
        - 系统盘扩容
        - 数据盘扩容
    - 费用
        - 按量付费
        - 包年包月
        - 竞价实例
    - 快照
    - 弹性ip
RDS: 数据库
    - mysql
    - redis
OSS：存储
    - 文件
    - 生命周期
    - 访问权限
    - 域名加速
RAM：访问控制
    - 子账号授权
    - ack编程访问
SLB：负载均衡
    - 后端服务器
    - 监听端口
    - 健康检查
VPC：内网管理
    - 子网规划
    - 安全组
OOS: 运维编排
    - 批量更换弹性ip
    - 定时执行运维任务
CDN：内容分发网络




批量在上海A区创建一百台ecs，型号为ecs.n2.small，系统盘50G，镜像为centos7付费模式为按量付费，绑定弹性ip，弹性ip为按流量计费，峰值为10M，绑定安全组，允许80 443 22端口访问