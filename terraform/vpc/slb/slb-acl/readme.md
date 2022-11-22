terraform init

cat main.tf
```sh
resource "alicloud_slb_acl" "example" {
}
```
导入已有配置
```sh
terraform import alicloud_slb_acl.example acl-xxxxx
```
查看配置
```sh
terraform state show  alicloud_slb_acl.example
```
导出配置到main.tf
```sh
terraform state show alicloud_slb_acl.example > main.tf
```
删除带有id=xxx的那一行
```sh
terraform plan
```
修改main.tf
既可以给原有的acl添加IP。注意是CIDR的格式