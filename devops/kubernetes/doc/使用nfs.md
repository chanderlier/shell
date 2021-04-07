k8s 使用nfs作为pv、pvc
安装nfs
10.0.10.177
```sh
yum install -y nfs-utils
yum install -y rpcbind
systemctl enable rpcbind
systemctl start rpcbind
systemctl start nfs-server
systemctl start nfs-secure-server
systemctl enable nfs-server
systemctl enable nfs-secure
systemctl start nfs-secure
```
```sh
mkdir /data
```
```sh
cat > /etc/exports <<EOF
/data 10.0.10.0/24 (rw,async)
EOF
```
```sh
systemctl reload nfs
```
check
```sh
showmount -e 10.0.10.177
```

k8s node节点安装nfs
```sh
yum install -y nfs-utils
```
```sh
mkdir /php-data
```
```sh
showmount -e 10.0.10.177
```
```sh
mount -t nfs 10.0.10.177:/data /php-data
```

```sh
cat php-pv.yaml
```
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name:  pv1
spec:
  capacity: 
    storage: 1Gi
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Recycle
  nfs:
    path: /data
    server: 10.0.10.177
```
```sh
cat php-pvc.yaml
```
```yaml
apiVersion: v1
metadata:
  name: php-pvc
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 10Gi
  selector:
    matchLabels:
      pv: pv1
```