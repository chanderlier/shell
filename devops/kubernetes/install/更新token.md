```sh
kubeadm token generate
```
som0bg.sh28pwnurpcbjdpq
```sh
kubeadm token create som0bg.sh28pwnurpcbjdpq --print-join-command --ttl=0
```
kubeadm join 10.0.10.180:6443 --token som0bg.sh28pwnurpcbjdpq --discovery-token-ca-cert-hash sha256:36437679b8fa46d03ec17c605bedc9916cb64a3667cfe9860bc54b2332eceee8