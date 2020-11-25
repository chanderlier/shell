download aliyun cli 
```sh
wget https://github.com/aliyun/aliyun-cli/releases/download/v3.0.62/aliyun-cli-linux-3.0.62-amd64.tgz
```
解压
```sh
tartar xzvf aliyun-cli-linux-3.0.62-amd64.tgz
```
执行如下命令，将aliyun程序移动到到/usr/local/bin目录中。
```sh
mv aliyun /usr/local/bin
```



init
```sh
aliyun configure
aliyun Access Key ID [None]: xxxxx
aliyun Access Key Secret [None]: xxxxx
Default Region Id [None]: cn-hangzhou # 地域ID
Default Output Format [json]: json (Only supports JSON) # 目前仅支持JSON
Default Language [zh|en]: en # 在这里选择英语
```
##ECS
获取本地实例信息
```sh
aliyun ecs DescribeInstances --output cols=InstanceId,InstanceName rows=Instances.Instance[]
```

```sh
InstanceId             | InstanceName
----------             | ------------
i-uf6hf4qqoc03n42juo3j | master
i-uf68987vinv7y5m4d49b | dieser-s
```
查询实例ID为i-uf6hf4qqoc03n42juo3j的实例信息。
```sh
aliyun ecs DescribeInstances --RegionId cn-shanghai --InstanceIds '["i-uf6hf4qqoc03n42juo3j"]' --output cols=InstanceId,InstanceName,Description,ImageId,Status rows=Instances.Instance[]
```
```sh
InstanceId             | InstanceName | Description | ImageId                                 | Status
----------             | ------------ | ----------- | -------                                 | ------
i-uf6hf4qqoc03n42juo3j | master       |             | centos_8_1_x64_20G_alibase_20200519.vhd | Running
```
查询在上海区域，运行的实例ID
```sh
aliyun ecs DescribeInstances --RegionId cn-shanghai  --Status Running --output cols=Instances.Instance[].InstanceId
```

```sh
[i-uf6hf4qqoc03n42juo3j i-uf68987vinv7y5m4d49b]
```
停止运行中的ECS实例。
本示例中停止一台运行中的按量付费ECS实例i-uf6hf4qqoc03n42juo3j，设置停止后继续计费，并且预检查后正常停止ECS实例。
```sh
aliyun ecs StopInstance --InstanceId i-uf6hf4qqoc03n42juo3j  --ForceStop false --StoppedMode KeepCharging --DryRun false
```
##VPC
通过DescribeVpcs API查询专有网络VPC ID。
```sh
aliyun vpc DescribeVpcs --RegionId cn-shanghai --output cols=Vpcs.Vpc[].VpcId
```
```sh
Vpcs.Vpc[].VpcId
----------------
[vpc-uf60iohxk0eupdtd891br vpc-uf644zy09vxmz984rou1c]
```
创建一个专有网络VPC类型的安全组。
```sh
aliyun ecs CreateSecurityGroup --RegionId cn-shanghai --Description demo --SecurityGroupName demo --VpcId vpc-bp1vwnn14rqpyiczj**** --SecurityGroupType normal
```

查询上海地区，网络类型为专有网络VPC，所有安全组的基本信息。
```sh
aliyun ecs DescribeSecurityGroups --RegionId cn-shanghai --NetworkType vpc --DryRun false --output cols=SecurityGroupName,Description,VpcId,Tags rows=SecurityGroups.SecurityGroup[]
```
```sh
SecurityGroupName                                                         | Description                                                     | VpcId                     | Tags
-----------------                                                         | -----------                                                     | -----                     | ----
alicloud-cs-auto-created-security-group-c2630bc9ccf7e4435b0621d2acafd4fef | security group of ACS Cluster c2630bc9ccf7e4435b0621d2acafd4fef | vpc-uf644zy09vxmz984rou1c | map[Tag:[]]
refrain                                                                   |                                                                 | vpc-uf644zy09vxmz984rou1c | map[Tag:[]]
refrain                                                                   |                                                                 | vpc-uf644zy09vxmz984rou1c | map[Tag:[]]
refrain                                                                   |                                                                 | vpc-uf644zy09vxmz984rou1c | map[Tag:[]]
ngw-uf6gyjh239nv9lhbdsedd_user_ep_security_group                          |                                                                 | vpc-uf644zy09vxmz984rou1c | map[Tag:[]]
```
根据安全组所在的专有网络VPC ID查询安全组的信息。
```sh
aliyun ecs DescribeSecurityGroups --RegionId cn-shanghai --VpcId  vpc-uf644zy09vxmz984rou1c --NetworkType vpc --DryRun false --output cols=SecurityGroupId,SecurityGroupName,Tags rows=SecurityGroups.SecurityGroup[]
```
```sh
SecurityGroupId         | SecurityGroupName                                                         | Tags
---------------         | -----------------                                                         | ----
sg-uf6bhe673f5qbfvvlwgn | alicloud-cs-auto-created-security-group-c2630bc9ccf7e4435b0621d2acafd4fef | map[Tag:[]]
sg-uf69mhjl9dewrlgizsih | refrain                                                                   | map[Tag:[]]
sg-uf6f7r0l1jg6z4picha2 | refrain                                                                   | map[Tag:[]]
sg-uf68wlmty40zbadeg219 | refrain                                                                   | map[Tag:[]]
sg-uf65oxto4re64dhzjmzi | ngw-uf6gyjh239nv9lhbdsedd_user_ep_security_group                          | map[Tag:[]]
```
```sh
aliyun ecs DescribeSecurityGroupAttribute --RegionId cn-shanghai --SecurityGroupId sg-uf68wlmty40zbadeg219 --Direction ingress --output cols=SourceCidrIp,NicType,PortRange,Direction,IpProtocol,Policy rows=Permissions.Permission[]
```
截取部分信息
```sh
SourceCidrIp       | NicType  | PortRange | Direction | IpProtocol | Policy
------------       | -------  | --------- | --------- | ---------- | ------
0.0.0.0/0          | intranet | 80/80     | ingress   | TCP        | Accept
0.0.0.0/0          | intranet | 443/443   | ingress   | TCP        | Accept
0.0.0.0/0          | intranet | 22/22     | ingress   | TCP        | Accept
0.0.0.0/0          | intranet | -1/-1     | ingress   | ICMP       | Accept
```