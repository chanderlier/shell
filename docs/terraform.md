## 安装
```sh
wget https://releases.hashicorp.com/terraform/0.13.5/terraform_0.13.5_linux_amd64.zip
```
解压
```sh
unzip terraform_0.13.5_linux_amd64.zip
```
将应用放置到/usr/local/bin
```sh
mv terraform_0.13.5_linux_amd64 /usr/local/bin/terraform
```
确认
```sh
terraform
```
终端部分信息如下
```sh
Usage: terraform [-version] [-help] <command> [args]

The available commands for execution are listed below.
The most common, useful commands are shown first, followed by
less common or more advanced commands. If you are just getting
started with Terraform, stick with the common commands. For the
other commands, please read the help and docs before usage.

Common commands:
    apply              Builds or changes infrastructure
    console            Interactive console for Terraform interpolations
    destroy            Destroy Terraform-managed infrastructure
    env                Workspace management
```

配置信息
```sh
export ALICLOUD_ACCESS_KEY="LTAIUrZCw3********"
export ALICLOUD_SECRET_KEY="zfwwWAMWIAiooj14GQ2*************"
export ALICLOUD_REGION="cn-shanghai"
```

## ECS
通过terraform快速创建一个ECS实例，并设置好相应的服务,例如VPC
```sh
cat terraform.tf
```
```sh
resource "alicloud_vpc" "vpc" {
  name       = "tf_test"
  cidr_block = "172.16.0.0/12"
}

resource "alicloud_vswitch" "vsw" {
  vpc_id            = alicloud_vpc.vpc.id
  cidr_block        = "172.16.0.0/21"
  availability_zone = "cn-shanghai-a"
}
resource "alicloud_security_group" "default" {
  name = "default"
  vpc_id = alicloud_vpc.vpc.id
}

resource "alicloud_security_group_rule" "allow_all_tcp" {
  type              = "ingress"
  ip_protocol       = "tcp"
  nic_type          = "intranet"
  policy            = "accept"
  port_range        = "1/65535"
  priority          = 1
  security_group_id = alicloud_security_group.default.id
  cidr_ip           = "0.0.0.0/0"
}
resource "alicloud_instance" "instance" {
  # cn-shanghai
  availability_zone = "cn-shanghai-a"
  security_groups = alicloud_security_group.default.*.id

  # series III
  instance_type        = "ecs.n2.small"
  system_disk_category = "cloud_efficiency"
  image_id             = "ubuntu_18_04_64_20G_alibase_20190624.vhd"
  instance_name        = "test"
  vswitch_id = alicloud_vswitch.vsw.id
  #internet_max_bandwidth_out =10
  password = "password!@1234"
}
```
创建实例
```sh
terraform apply
```
查看实例
```sh
terraform show
```
销毁实例
```sh
terraform destroy
```
## RAM
通过terraform创建一个RAM用户
### 方式一
```sh
cat terraform.tf
```
```sh
provider "alicloud" {
}
//创建RAM用户，包含用户名、昵称、手机号、邮箱、备注、
resource "alicloud_ram_user" "user" {
  name         = "user_test"
  display_name = "testAccount"
  mobile       = "86-18888888888"
  email        = "localhost@example.com"
  comments     = "jojo"
  force        = true
}
//指定用户名密码登陆控制台
resource "alicloud_ram_login_profile" "profile" {
  user_name = alicloud_ram_user.user.name //这边等同于user_test
  password  = "Password!@1234" //控制台登陆的密码
}
//创建访问密钥AccessKey
resource "alicloud_ram_access_key" "ak" {
  user_name   = alicloud_ram_user.user.name
  secret_file = "accesskey.txt" //创建secret，保存为accesskey.txt
}
//创建ram群组
resource "alicloud_ram_group" "group" {
  name     = "test_ram_group"
  comments = "this is a group comments."
  force    = true
}
//将用户加入用户组
resource "alicloud_ram_group_membership" "membership" {
  group_name = alicloud_ram_group.group.name
  user_names = [alicloud_ram_user.user.name]
}
```

### 方式二
```sh
module "ram_user" {
   // 引用module源地址
   source = "terraform-alicloud-modules/ram/alicloud"
   // RAM用户名
   name = "test_user"
   // 是否创建控制台登录凭证
   create_ram_user_login_profile = true
   // 控制台登录密码
   password = "Password!@1234"
   // 是否创建accesskey
   create_ram_access_key = true
   // 是否赋予管理员权限
   is_admin = true
 }
 ```
