有时候会在初始化的时候遇到一下问题  
terraform init  
```sh
Initializing the backend...

Initializing provider plugins...
- Finding latest version of hashicorp/alicloud...
Provider installation was canceled by an interrupt signal.
➜  ecstest vim provider.tf
➜  ecstest terraform init

Initializing the backend...

Initializing provider plugins...
- Finding aliyun/alicloud versions matching "1.143.0"...
- Installing aliyun/alicloud v1.143.0...
╷
│ Error: Failed to install provider
│
│ Error while installing aliyun/alicloud v1.143.0: Get "https://github.com/aliyun/terraform-provider-alicloud/releases/download/v1.143.0/terraform-provider-alicloud_1.143.0_darwin_arm64.zip": EOF
```
为了防止这样，并节约以后部署的时间，不需要每次都要重新下载，这里介绍一个方法。  
以alicloud为例，首先去https://releases.hashicorp.com/
下载对应的插件的压缩包，然后解压放到指定的目录下。
```sh
mv terraform-provider-alicloud_v1.143.0 $HOME/.terraform.d/plugins/registry.terraform.io/hashicorp/alicloud/1.143.0/darwin_arm64/
```
provider.tf
```tf
provider "alicloud" {
    region           = "cn-qingdao"
    access_key       = "LT********N3x"
    secret_key       = "Uju8*************orcBGYLy"
}
```
然后就可以
```sh
terraform init 
```

