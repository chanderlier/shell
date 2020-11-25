安装
```sh
wget https://releases.hashicorp.com/terraform/0.13.5/terraform_0.13.5_linux_amd64.zip
```
```sh
unzip terraform_0.13.5_linux_amd64.zip
```
```sh
mv 
```
通过terraform快速创建一个ECS实例，并设置好相应的服务,例如VPC
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