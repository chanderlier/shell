### 简介
gitlab使用ci-cd功能，需要gitlab-runner的支持。gitlab-runner可以和gitlab安装在同一台服务器上，如果对性能要求较高的话，可以在不同的服务器上安装gitlab-runner，然后注册到gitlab上即可。

### 安装gitlab-runner

```sh
curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.rpm.sh" | sudo bash
export GITLAB_RUNNER_DISABLE_SKEL=true
sudo -E yum install -y gitlab-runner
```
注册
gitlab-runner register
```sh
Runtime platform                                    arch=amd64 os=linux pid=86204 revision=7f7a4bb0 version=13.11.0
Running in system-mode.                            
                                                   
Enter the GitLab instance URL (for example, https://gitlab.com/):
http://git.dieser.com:8888/ # gitlab域名
Enter the registration token:
wTM22czMMpPSrUuV-C54        # token
Enter a description for the runner:
[master]: test
Enter tags for the runner (comma-separated):
test    
Registering runner... succeeded                     runner=wTM54czM
Enter an executor: custom, parallels, virtualbox, docker+machine, docker-ssh+machine, docker, docker-ssh, shell, ssh, kubernetes:
shell  # 根据自己的需要选择对应的executor，此处我选择的是shell，也可以用docker、kubernetes 
Runner registered successfully. Feel free to start it, but if it's running already the config should be automatically reloaded! 
```
确认
```sh
gitlab-runner status 
Runtime platform                                    arch=amd64 os=linux pid=90228 revision=7f7a4bb0 version=13.11.0
```
此处gitlab-runner就已经安装完毕
以前端后端数据组举例。
通过
gitlab-runner register命令可以注册tag为frunner,brunner,drunner三个runner。使用一段时间后，我们发现发布会变慢。后面决定再加一台服务器，安装gitlab-runner tag保持一致即可。即frunner，brunner分布在两台服务器上，有效提升了项目发布的效率。
