目标：创建一个私有读写的bucket，创建用户并使用阿里云sts
大致需要一下几步
1: 创建oss，设置访问权限
2: 创建RAM用户
3: 创建访问策略
4: 创建角色
5: 绑定RAM用户和访问策略，绑定角色和访问策略
首先创建一个目录，进入到目录后，创建配置文件
```sh
mkdir osstest && cd osstest
```
创建provider
```sh
vim provider.tf
```
```tf
provider "alicloud" {
    region           = "cn-shanghai"
    access_key       = "LTA**********NO2"
    secret_key       = "MOk8x0*********************wwff"
}
```
初始化
```sh
terraform init
```
创建oss，bucket权限为私有读写
```sh
vim createoss.tf
```
```tf
resource "alicloud_oss_bucket" "bucket-acl" {
  bucket = "osstest"
  acl    = "private"
}
```
创建ram用户
```sh
vim createuser.tf
```
```tf
resource "alicloud_ram_user" "user" {
  name         = "osstester"          # 用户名
  comments     = "oss test"
  force        = true    
}
resource "alicloud_ram_access_key" "ak" {
  user_name   = alicloud_ram_user.user.name
  secret_file = "accesskey.txt"                # 保存AccessKey的文件名
}
```
创建策略，此处为用户可以查看和下载osstest这个bucket的内容
```tf
resource "alicloud_ram_policy" "policy" {
  name     = "dieserpolicy"
  document = <<EOF
  {
    "Statement": [
      {
        "Action": [
          "oss:ListObjects", # 可以通过ossutils或者ossbrower查看指定BUCKET中的内容
          "oss:GetObject"   # 可以下载文件，如果需要上传文件的话，需要增加一个 oss:PutObject权限
        ],
        "Effect": "Allow",
        "Resource": [
          "acs:oss:*:*:refrain1234",
          "acs:oss:*:*:refrain1234/*"
        ]
      }
    ],
      "Version": "1"
  }
  EOF
  description = "this is a policy test"
  force = true
}
```

将ram.user和policy绑定
```tf
resource "alicloud_ram_user_policy_attachment" "attach" {
  policy_name = alicloud_ram_policy.policy.name
  policy_type = alicloud_ram_policy.policy.type
  user_name   = alicloud_ram_user.user.name
}
```
创建ram
```sh
vim createrole.tf
```
```tf
resource "alicloud_resource_manager_role" "role" {
  role_name                   = "ststest"
  assume_role_policy_document = <<EOF
     {
          "Statement": [
               {
                    "Action": "sts:AssumeRole",
                    "Effect": "Allow",
                    "Principal": {
                        "RAM":[
                                "acs:ram::1216403154769350:root"
                        ]
                    }
                }
          ],
          "Version": "1"
     }
     EOF
}
```
绑定role和policy
```tf
resource "alicloud_ram_role_policy_attachment" "attach" {
  policy_name = alicloud_ram_policy.policy.name
  policy_type = alicloud_ram_policy.policy.type
  role_name   = alicloud_resource_manager_role.role.role_name
}
```
后续如果有新项目要创建类似的，可以从文件中取出变量。