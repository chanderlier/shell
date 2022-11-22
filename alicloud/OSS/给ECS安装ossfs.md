install ossfs 
```sh
git clone https://github.com/aliyun/ossfs.git
cd ossfs/
./autogen.sh
./configure
make
make install
```
configure ossfs 
```sh
echo my-bucket:my-access-key-id:my-access-key-secret > /etc/passwd-ossfs
chmod 640 /etc/passwd-ossfs
```
```sh
mkdir /data
ossfs my-bucket /data -ourl=http://oss-cn-shanghai.aliyuncs.com 
```
if use VPC
```sh
ossfs my-bucket /data -ourl=http://oss-cn-shanghai-internal.aliyuncs.com
```