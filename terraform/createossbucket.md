目标：创建一个私有读写的bucket，创建用户并使用阿里云sts 
大致需要一下几步  
1：创建oss，设置访问权限  
2：创建RAM用户  
3： 创建访问策略  
4：创建角色  
5：绑定RAM用户和访问策略，绑定角色和访问策略  
首先创建一个目录，进入到目录后，创建配置文件
```sh
mkdir osstest && cd osstest
```
创建provider.tf
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
  policy_name     = "dieserpolicy"
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
          "acs:oss:*:*:osstest",
          "acs:oss:*:*:osstest/*"
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
  policy_name = alicloud_ram_policy.policy.policy_name
  policy_type = alicloud_ram_policy.policy.type
  user_name   = alicloud_ram_user.user.name
}
```
创建ram role用户
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
                                "acs:ram::12********9350:root"
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
  policy_name = alicloud_ram_policy.policy.policy_name
  policy_type = alicloud_ram_policy.policy.type
  role_name   = alicloud_resource_manager_role.role.role_name
}
```
完整的main.tf
```tf
resource "alicloud_oss_bucket" "bucket-acl" {
  bucket = "osstest"
  acl    = "private"
}
resource "alicloud_ram_user" "user" {
  name         = "osstester"          # 用户名
  comments     = "oss test"
  force        = true    
}
resource "alicloud_ram_access_key" "ak" {
  user_name   = alicloud_ram_user.user.name
  secret_file = "accesskey.txt"                # 保存AccessKey的文件名
}
resource "alicloud_ram_policy" "policy" {
  policy_name     = "osspolicy"
  policy_document = <<EOF
  {
    "Statement": [
      {
        "Action": [
          "oss:ListObjects",  
          "oss:GetObject"    
        ],
        "Effect": "Allow",
        "Resource": [
          "acs:oss:*:*:osstest",
          "acs:oss:*:*:osstest/*"
        ]
      }
    ],
      "Version": "1"
  }
  EOF
  description = "this is a policy test"
  force = true
}
# 将ram.user和policy绑定
resource "alicloud_ram_user_policy_attachment" "attach" {
  policy_name = alicloud_ram_policy.policy.policy_name
  policy_type = alicloud_ram_policy.policy.type
  user_name   = alicloud_ram_user.user.name
}

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
                                "acs:ram::121********69350:root"
                        ]
                    }
                }
          ],
          "Version": "1"
     }
     EOF
}
# 将ram.role与policy绑定
resource "alicloud_ram_role_policy_attachment" "attach" {
  policy_name = alicloud_ram_policy.policy.policy_name
  policy_type = alicloud_ram_policy.policy.type
  role_name   = alicloud_resource_manager_role.role.role_name
}
```
后续如果有新项目要创建类似的，可以从终端输入变量。
先定义一个变量文件
```sh
vim var.tf
```
```tf
variable "ram_user_name" {
  type = string
  description = "ram user name"
}
variable "ram_role_name" {
  type = string
  description = "ram role name"
}
variable "ram_policy_name" {
  type = string
  description = "ram policy name"
}
variable "oss_bucket_name" {
  type = string
  description = "oss bucket name"
}
variable "ARN" {
  type = string
  description = "ARNID"
}
```
```tf
resource "alicloud_oss_bucket" "bucket-acl" {
  bucket = var.oss_bucket_name
  acl    = "private"
}
resource "alicloud_ram_user" "user" {
  name         = var.ram_user_name          # 用户名
  comments     = "oss test"
  force        = true
}
resource "alicloud_ram_access_key" "ak" {
  user_name   = alicloud_ram_user.user.name
  secret_file = "accesskey.txt"                # 保存AccessKey的文件名
}
resource "alicloud_ram_policy" "policy" {
  policy_name     = var.ram_policy_name
  policy_document = <<EOF
  {
    "Statement": [
      {
        "Action": [
          "oss:ListObjects",
          "oss:GetObject"
        ],
        "Effect": "Allow",
        "Resource": [
          "acs:oss:*:*:var.oss_bucket_name",
          "acs:oss:*:*:var.oss_bucket_name/*"
        ]
      }
    ],
      "Version": "1"
  }
  EOF
  description = "this is a policy test"
  force = true
}
# 将ram.user和policy绑定
resource "alicloud_ram_user_policy_attachment" "attach" {
  policy_name = alicloud_ram_policy.policy.policy_name
  policy_type = alicloud_ram_policy.policy.type
  user_name   = alicloud_ram_user.user.name
}

resource "alicloud_ram_role" "role" {
  name = var.ram_role_name
  document    = <<EOF
  {
    "Statement": [
      {
        "Action": "sts:AssumeRole",
        "Effect": "Allow",
        "Principal": {
          "RAM": [
            "${var.ARN}"
          ]
        }
      }
    ],
    "Version": "1"
  }
  EOF
  description = "this is a role test."
  force       = true
}
# 将ram.role与policy绑定
resource "alicloud_ram_role_policy_attachment" "attach" {
  policy_name = alicloud_ram_policy.policy.policy_name
  policy_type = alicloud_ram_policy.policy.type
  role_name   = alicloud_ram_role.role.name
}
```
编辑完成后，在终端输入
```sh
terraform plan
```
进行测试

第二种，定义好变量文件，直接引用。如果后期有类似的项目，可以新建一个文件夹，copy文件到新目录，修改terraform.tfvars文件，然后执行对应的命令生成资源即可。
如果制定.tfvars为terraform.tfvars，则执行命令时默认加载，如果是var.tfvars的话，则需要通过
```sh
terraform plan -var-file="var.tfvars"
```
去指定。
如果就只有.tfvars而没有varibles.tf，执行的时候会报错，因为找不到变量。
```sh
The root module does not declare a variable named "ARN" but a value was found in file "var.tfvars". If you meant to use this value, add a "variable" block to the configuration.
```
```sh
vim terraform.tfvars
```
```tfvars
 ram_user_name="tfuser",
 ram_role_name="tfrole",
 oss_bucket_name="tfossbucket",
 ram_policy_name="tframpolicy",
 ARN="acs:ram::1216******769350:root"
```
```sh
vim variables.tf
```
```tf
variable "ram_user_name" {
  type = string
  description = "ram user name"
}
variable "ram_role_name" {
  type = string
  description = "ram role name"
}
variable "ram_policy_name" {
  type = string
  description = "ram policy name"
}
variable "oss_bucket_name" {
  type = string
  description = "oss bucket name"
}
variable "ARN" {
  type = string
  description = "ARNID"
}
```
main.tf
```tf
resource "alicloud_oss_bucket" "bucket-acl" {
  bucket = var.oss_bucket_name
  acl    = "private"
}
resource "alicloud_ram_user" "user" {
  name         = var.ram_user_name          # 用户名
  comments     = "oss test"
  force        = true
}
resource "alicloud_ram_access_key" "ak" {
  user_name   = alicloud_ram_user.user.name
  secret_file = "accesskey.txt"                # 保存AccessKey的文件名
}
resource "alicloud_ram_policy" "policy" {
  policy_name     = var.ram_policy_name
  policy_document = <<EOF
  {
    "Statement": [
      {
        "Action": [
          "oss:ListObjects",
          "oss:GetObject"
        ],
        "Effect": "Allow",
        "Resource": [
          "acs:oss:*:*:var.oss_bucket_name",
          "acs:oss:*:*:var.oss_bucket_name/*"
        ]
      }
    ],
      "Version": "1"
  }
  EOF
  description = "this is a policy test"
  force = true
}
# 将ram.user和policy绑定
resource "alicloud_ram_user_policy_attachment" "attach" {
  policy_name = alicloud_ram_policy.policy.policy_name
  policy_type = alicloud_ram_policy.policy.type
  user_name   = alicloud_ram_user.user.name
}

resource "alicloud_ram_role" "role" {
  name = var.ram_role_name
  document    = <<EOF
  {
    "Statement": [
      {
        "Action": "sts:AssumeRole",
        "Effect": "Allow",
        "Principal": {
          "RAM": [
            "${var.ARN}"
          ]
        }
      }
    ],
    "Version": "1"
  }
  EOF
  description = "this is a role test."
  force       = true
}
# 将ram.role与policy绑定
resource "alicloud_ram_role_policy_attachment" "attach" {
  policy_name = alicloud_ram_policy.policy.policy_name
  policy_type = alicloud_ram_policy.policy.type
  role_name   = alicloud_ram_role.role.name
}
```
预览
```sh
terraform plan -var-file="var.tfvars"
```
创建资源
```sh
terraform apply -var-file="var.tfvars"
```
验证，确定没问题后,删除创建的资源
```sh
terraform destroy -var-file="var.tfvars"
```