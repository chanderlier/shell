[defaults]
host_key_checking=false #ssh登录免去验证  
iventory = hosts       #主机目录  
forks = 30             #并发数  
private_key_file = /Users/dieser/.ssh/id_rsa #私钥文件  
remote_user = root                          #远程用户名  
gathering = smart   #修改收集远程主机信息策略  
timeout=30  #设置超时时间  
