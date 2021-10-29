# install
docker pull prom/pushgateway
docker run -d -p 9091:9091 prom/pushgateway
#  edit prometheus.yml
```yaml
...
- job_name: 'pushgateway'
    static_configs:
      - targets: ['172.30.12.167:9091']
        labels:
          instance: pushgateway
```
