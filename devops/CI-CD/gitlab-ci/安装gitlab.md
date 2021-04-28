# 在centos7服务器上安装gitlab
gitlab要求4G内存
## 安装
在centos最小化安装后，基本也是包含以下几项
```sh
sudo yum install -y curl policycoreutils-python openssh-server perl
sudo systemctl enable sshd
sudo systemctl start sshd
sudo yum install postfix
sudo systemctl enable postfix
sudo systemctl start postfix
```
### 开通防火墙
```sh
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo systemctl reload firewalld
```
### 或者也可以直接关闭防火墙
```sh
systemctl disable firewalld
systemctl stop firewalld
```
### 执行安装脚本
```sh
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | sudo bash
```
### 安装最新版的gitlab-ce
```sh
sudo yum install -y gitlab-ce
```
## 配置
通过修改/etc/gitlab/gitlab.rb中的配置，然后执行
```sh
gitlab-ctl reconfigure
```
### 修改gitlab的配置
#### 修改时区
```sh
# gitlab_rails['time_zone'] = 'UTC' -> gitlab_rails['time_zone'] = 'Asia/Shanghai'
```
如果我们是在单台服务器上安装gitlab，那么可以不需要修改端口，如果和jenkins等工具都安装在一个服务器上，那么需要修改某些服务的端口。
修改gitlab端口
```sh
# unicorn['port'] = 8080 -> unicorn['port'] = 7788
```
#### 修改EXTERNAL_URL的值服务器为域名或ip
```sh
external_url 'http://gitlab.example.com' -> external_url 'https://git.dieser.com:<port>'
```
#### 修改gitlab默认储存目录
默认配置文件
```sh
### For setting up different data storing directory
###! Docs: https://docs.gitlab.com/omnibus/settings/configuration.html#storing-git-data-in-an-alternative-directory
###! **If you want to use a single non-default directory to store git data use a
###!   path that doesn't contain symlinks.**
# git_data_dirs({
#   "default" => {
#     "path" => "/mnt/nfs-01/git-data"
#    }
# })
```
修改后的配置文件
```sh
### For setting up different data storing directory
###! Docs: https://docs.gitlab.com/omnibus/settings/configuration.html#storing-git-data-in-an-alternative-directory
###! **If you want to use a single non-default directory to store git data use a
###!   path that doesn't contain symlinks.**
git_data_dirs({
   "default" => {
     "path" => "/data/gitlab/git-data"
    }
 })
```
#### 备份
默认配置文件
```sh
### Backup Settings
###! Docs: https://docs.gitlab.com/omnibus/settings/backups.html

# gitlab_rails['manage_backup_path'] = true
# gitlab_rails['backup_path'] = "/var/opt/gitlab/backups" # 备份存放目录

###! Docs: https://docs.gitlab.com/ee/raketasks/backup_restore.html#backup-archive-permissions
# gitlab_rails['backup_archive_permissions'] = 0644

# gitlab_rails['backup_pg_schema'] = 'public'

###! The duration in seconds to keep backups before they are allowed to be deleted
# gitlab_rails['backup_keep_time'] = 604800 #备份存放时间，默认为七天

# gitlab_rails['backup_upload_connection'] = {  # 备份上传到云服务商
#   'provider' => 'AWS', # 此处为AWS，也可以是Azure、GCP、aliyun等
#   'region' => 'eu-west-1', # aws地域
#   'aws_access_key_id' => 'AKIAKIAKI',# 创建的access_key_id
#   'aws_secret_access_key' => 'secret123', # 创建的secret_access_key
#   # # If IAM profile use is enabled, remove aws_access_key_id and aws_secret_access_key
#   'use_iam_profile' => false
# }
# gitlab_rails['backup_upload_remote_directory'] = 'my.s3.bucket'
# gitlab_rails['backup_multipart_chunk_size'] = 104857600
```
修改后的配置文件
```sh
### Backup Settings
###! Docs: https://docs.gitlab.com/omnibus/settings/backups.html

gitlab_rails['manage_backup_path'] = true
gitlab_rails['backup_path'] = "/data/gitlab/backups"

###! Docs: https://docs.gitlab.com/ee/raketasks/backup_restore.html#backup-archive-permissions
# gitlab_rails['backup_archive_permissions'] = 0644

# gitlab_rails['backup_pg_schema'] = 'public'

###! The duration in seconds to keep backups before they are allowed to be deleted
gitlab_rails['backup_keep_time'] = 604800

gitlab_rails['backup_upload_connection'] = {
   'provider' => 'AWS',
   'region' => 'eu-west-1',
   'aws_access_key_id' => 'AKIAKIAKI',
   'aws_secret_access_key' => 'secret123',
   # # If IAM profile use is enabled, remove aws_access_key_id and aws_secret_access_key
   'use_iam_profile' => false
 }
 gitlab_rails['backup_upload_remote_directory'] = 'my.s3.bucket'
 gitlab_rails['backup_multipart_chunk_size'] = 104857600
```

#### 配置SMTP服务器
默认配置文件
```sh
# gitlab_rails['smtp_enable'] = true # 启用smtp
# gitlab_rails['smtp_address'] = "smtp.server" # smtp服务器
# gitlab_rails['smtp_port'] = 465 # smtp端口
# gitlab_rails['smtp_user_name'] = "smtp user" # 用户名
# gitlab_rails['smtp_password'] = "smtp password" #客户端密码
# gitlab_rails['smtp_domain'] = "example.com"
# gitlab_rails['smtp_authentication'] = "login" # 认证方式
# gitlab_rails['smtp_enable_starttls_auto'] = true 
# gitlab_rails['smtp_tls'] = false
# gitlab_rails['gitlab_email_from'] = 'example@example.com' #邮件发送者地址
# gitlab_rails['gitlab_email_display_name'] = 'Example'
# gitlab_rails['gitlab_email_reply_to'] = 'noreply@example.com' # 邮件发送者地址
```
修改后配置文件,使用腾讯企业邮箱
```sh
gitlab_rails['smtp_enable'] = true
gitlab_rails['smtp_address'] = "smtp.exmail.qq.com"
gitlab_rails['smtp_port'] = 25
gitlab_rails['smtp_user_name'] = "smtp user"
gitlab_rails['smtp_password'] = "smtp password"
# gitlab_rails['smtp_domain'] = "example.com"
gitlab_rails['smtp_authentication'] = "login"
gitlab_rails['smtp_enable_starttls_auto'] = true
gitlab_rails['smtp_tls'] = false
gitlab_rails['gitlab_email_from'] = 'example@dieser.com'
# gitlab_rails['gitlab_email_display_name'] = 'Example'
gitlab_rails['gitlab_email_reply_to'] = 'noreply@dieser.com'
```
#### 修改redis，默认配置为本地
```sh
#### Redis TCP connection
# gitlab_rails['redis_host'] = "127.0.0.1"
# gitlab_rails['redis_port'] = 6379
# gitlab_rails['redis_ssl'] = false
# gitlab_rails['redis_password'] = nil
# gitlab_rails['redis_database'] = 0
# gitlab_rails['redis_enable_client'] = true
```
修改后的配置文件
```sh
#### Redis TCP connection
gitlab_rails['redis_host'] = "redis.dieser.com"
gitlab_rails['redis_port'] = 6379
gitlab_rails['redis_ssl'] = false
gitlab_rails['redis_password'] = 12345qwert
gitlab_rails['redis_database'] = 1
gitlab_rails['redis_enable_client'] = true
```