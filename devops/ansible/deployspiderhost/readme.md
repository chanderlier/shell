查看hosts文件中，server组的连通情况
```sh
ansible -i hosts server -m ping
```
查看hosts文件中，vps组的连通情况
```sh
ansible -i hosts vps -m ping
```
对，在hosts文件中，主机别名为vps001执行main.yaml
```sh
ansible-playbook -i hosts --limit 'vps001' main.yaml
```
对，在hosts文件中，主机别名不为vps002的其他主机执行main.yaml
```sh
ansible-playbook -i hosts --limit '!vps002' main.yaml
```
对，在hosts文件中，主机别名为TSVPS014*，TSVPS016*,TSVPS017*的其他主机执行main.yaml
```sh
ansible-playbook main.yaml -i hosts --limit 'TSVPS014*:TSVPS016*:TSVPS017*'
```
检测目标主机是否有网
```sh
ansible -i hosts server  -m command -a "ping -c 1 www.baidu.com"|grep FAILED
```