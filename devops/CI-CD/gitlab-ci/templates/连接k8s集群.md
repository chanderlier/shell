项目->运维->Kubernetes  
添加k8s集群，Add existing cluster  
Kubernetes 集群名称  
test  
环境范围  
*   
API地址 
```sh
kubectl cluster-info | grep -E 'Kubernetes master|Kubernetes control plane' | awk '/http/ {print $NF}'
```


CA证书
```sh
kubectl get secrets |grep default-token
default-token-wd4mq                kubernetes.io/service-account-token   3      121d
```
get ca.pem
```sh
kubectl get secret default-token-wd4mq  -o jsonpath="{['data']['ca\.crt']}" | base64 --decode
```

```sh
cat > gitlab-admin-service-account.yaml <<EOF
apiVersion: v1
kind: ServiceAccount
metadata:
  name: gitlab
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: gitlab-admin
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
  - kind: ServiceAccount
    name: gitlab
    namespace: kube-system
EOF
```
```sh
kubectl apply -f gitlab-admin-service-account.yaml
```
get token 
```sh
kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep gitlab | awk '{print $1}')
```