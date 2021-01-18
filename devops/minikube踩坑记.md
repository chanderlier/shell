```sh
minikube addons list
```
```sh
|         ADDON NAME          | PROFILE  |    STATUS    |
|-----------------------------|----------|--------------|
| ambassador                  | minikube | disabled     |
| csi-hostpath-driver         | minikube | disabled     |
| dashboard                   | minikube | disabled     |
| default-storageclass        | minikube | enabled ✅   |
| efk                         | minikube | enabled ✅   |
| freshpod                    | minikube | disabled     |
| gcp-auth                    | minikube | disabled     |
| gvisor                      | minikube | disabled     |
| helm-tiller                 | minikube | enabled ✅   |
| ingress                     | minikube | disabled     |
| ingress-dns                 | minikube | disabled     |
| istio                       | minikube | disabled     |
| istio-provisioner           | minikube | disabled     |
| kubevirt                    | minikube | disabled     |
| logviewer                   | minikube | disabled     |
| metallb                     | minikube | disabled     |
| metrics-server              | minikube | disabled     |
| nvidia-driver-installer     | minikube | disabled     |
| nvidia-gpu-device-plugin    | minikube | disabled     |
| olm                         | minikube | disabled     |
| pod-security-policy         | minikube | disabled     |
| registry                    | minikube | disabled     |
| registry-aliases            | minikube | disabled     |
| registry-creds              | minikube | disabled     |
| storage-provisioner         | minikube | enabled ✅   |
| storage-provisioner-gluster | minikube | disabled     |
| volumesnapshots             | minikube | disabled    
```
可以看到自带了很多插件。enable的为已启用，disable表示未安装/未启用。
比如需要使用EFK（elasticsearch+filebeats+kibana）
可以直接输入
```sh
minikube addons enable efk
```
```sh
[dieser@s-01 ~]$ minikube addons enable efk
* The 'efk' addon is enabled
[dieser@s-01 ~]$ minikube addons enable helm-tiller
* The 'helm-tiller' addon is enabled
```
但是比如ingress
```sh
[dieser@s-01 ~]$ minikube addons enable ingress
* Verifying ingress addon...
```
通过kubectl get pods --all-namespaces 
```sh
kube-system   ingress-nginx-admission-create-2p8rl        0/1     Completed           0          12m
kube-system   ingress-nginx-admission-patch-mc7wt         0/1     Completed           0          12m
kube-system   ingress-nginx-controller-799c9469f7-9wqhn   0/1     ImagePullBackOff    0          12m
```
可以判断是镜像文件拉取失败

```sh
ifconfig
```
昨天的信息
```sh
br-11b6d88166e9: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 192.168.49.2  netmask 255.255.255.0  broadcast 0.0.0.0
        inet6 fe80::42:bdff:fe53:b0e2  prefixlen 64  scopeid 0x20<link>
        ether 02:42:bd:53:b0:e2  txqueuelen 0  (Ethernet)
        RX packets 10399  bytes 1636917 (1.5 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 10399  bytes 1636917 (1.5 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

```

今天的信息
```sh
minikube ip
```
```sh
192.168.49.2
```

```sh
br-11b6d88166e9: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 192.168.49.1  netmask 255.255.255.0  broadcast 0.0.0.0
        inet6 fe80::42:bdff:fe53:b0e2  prefixlen 64  scopeid 0x20<link>
        ether 02:42:bd:53:b0:e2  txqueuelen 0  (Ethernet)
        RX packets 10399  bytes 1636917 (1.5 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 10399  bytes 1636917 (1.5 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

```
导致的结果就是无法正常通信

```sh
kubectl get pods --all-namespaces
```

```sh
The connection to the server 192.168.49.2:8443 was refused - did you specify the right host or port?

```
重启报错信息
```sh
[dieser@s-01 root]$ minikube stop
* Stopping node "minikube"  ...
* Powering off "minikube" via SSH ...
* 1 nodes stopped.
[dieser@s-01 root]$ minikube start
* minikube v1.14.1 on Alibaba 2.1903
* Using the docker driver based on existing profile
* Starting control plane node minikube in cluster minikube
* Restarting existing docker container for "minikube" ...
* minikube 1.14.2 is available! Download it: https://github.com/kubernetes/minikube/releases/tag/v1.14.2
* To disable this notice, run: 'minikube config set WantUpdateNotification false'

! StartHost failed, but will try again: provision: get ssh host-port: get port 22 for "minikube": docker container inspect -f "'{{(index (index .NetworkSettings.Ports "22/tcp") 0).HostPort}}'" minikube: exit status 1
stdout:


stderr:
Template parsing error: template: :1:11: executing "" at <index .NetworkSettings.Ports "22/tcp">: error calling index: index of untyped nil

* Restarting existing docker container for "minikube" ...
* Failed to start docker container. Running "minikube delete" may fix it: provision: get ssh host-port: get port 22 for "minikube": docker container inspect -f "'{{(index (index .NetworkSettings.Ports "22/tcp") 0).HostPort}}'" minikube: exit status 1
stdout:


stderr:
Template parsing error: template: :1:11: executing "" at <index .NetworkSettings.Ports "22/tcp">: error calling index: index of untyped nil

E1030 18:23:56.035259 2020684 out.go:286] unable to execute Failed to start host: provision: get ssh host-port: get port 22 for "minikube": docker container inspect -f "'{{(index (index .NetworkSettings.Ports "22/tcp") 0).HostPort}}'" minikube: exit status 1
stdout:


stderr:
Template parsing error: template: :1:11: executing "" at <index .NetworkSettings.Ports "22/tcp">: error calling index: index of untyped nil
: html/template:Failed to start host: provision: get ssh host-port: get port 22 for "minikube": docker container inspect -f "'{{(index (index .NetworkSettings.Ports "22/tcp") 0).HostPort}}'" minikube: exit status 1
stdout:


stderr:
Template parsing error: template: :1:11: executing "" at <index .NetworkSettings.Ports "22/tcp">: error calling index: index of untyped nil
: "\"" in attribute name: "\"22/tcp\">: error calling index: " - returning raw string.

X Exiting due to GUEST_PROVISION: Failed to start host: provision: get ssh host-port: get port 22 for "minikube": docker container inspect -f "'{{(index (index .NetworkSettings.Ports "22/tcp") 0).HostPort}}'" minikube: exit status 1
stdout:


stderr:
Template parsing error: template: :1:11: executing "" at <index .NetworkSettings.Ports "22/tcp">: error calling index: index of untyped nil

* 
* If the above advice does not help, please let us know: 
  - https://github.com/kubernetes/minikube/issues/new/choose

```