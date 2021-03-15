Bucket
## 权限
权限大致分为两大块，一方面我们可以在oss->bucket中设置授权，一方面，我们可以在访问控制中管理权限和授权对象
权限值 中文名称    权限对访问者的限制
public-read-write   公共读写    任何人（包括匿名访问）都可以对该Bucket中的Object进行读、写、删除操作；所有这些操作产生的费用由该Bucket的Owner承担，请慎用该权限。  
public-read 公共读，私有写 只有该Bucket的Owner或者授权对象可以对存放在其中的Object进行写、删除操作；任何人（包括匿名访问）可以对Object进行读操作。  
private 私有读写    只有该Bucket的Owner或者授权对象可以对存放在其中的Object进行读、写、删除操作；其他人在未经授权的情况下无法访问该Bucket内的 Object。  
如果bucket内的资源只是服务器之间交互，单纯的展示里面的资源，我们可以将其设置为私有读写。
如果bucket内的资源，用户可以读，仅特定对象可以进行读、写、删除等操作，那么我们可以将其设置为公共读，私有写。
如果bucket内的资源，所有对象都可以进行读写操作（一般这种需求很少，需要附上说明），那么我们将其设置为公共读写。

下面以一个名为dieser的用户，和一个叫做test的bucket举例。其中test中含有test1和test2的前缀。test1和test2继承bucket的权限。bucket中没有文件夹这一概念。  
linux中mkdir -p test/test1 类似等价于test bucket中新建目录 test1，但实际上只是有了一个名词为test1的前缀。  
bucket acl为公共读，私有写。
现在test允许所有人可读，dieser这个用户拥有所有权限，但禁止删除bucket内资源。我们可以在bucket中授权子用户dieser访问test内的的所有资源。
通过访问控制的话
我们可以新建一个权限
```json
{
    "Statement": [
        {
            "Action": [
                "oss:*"
            ],
            "Effect": "Allow",
            "Resource": [
                "acs:oss:*:*:test/*"
            ]
        },
        {
            "Effect": "Deny",
            "Action": [
                "oss:DeleteObject"
            ],
            "Resource": [
                "acs:oss:*:*:test/*"
            ]
        }
    ],
    "Version": "1"
}
```
授权给dieser用户
如果bucket acl是私有读写的话。那么即使我们给dieser授权了，我们也无法通过OSS Browser等软件访问里面的资源。
我们无法通过在访问控制中给指定用户增加权限的方式，访问一个bucket acl为私有读写的bucket中的资源。