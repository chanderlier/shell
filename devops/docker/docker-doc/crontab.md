在docker中使用crontab
```Dockerfile
FROM centos:centos7.5.1804
RUN yum update -y \
    && yum install -y epel-release \
    vixie-cron \
    crontabs \
    && yum clean all \
    && rm -rf /var/cache/yum/*
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/shanghai" > /etc/timezone
RUN sed -i '/session    required   pam_loginuid.so/c\#session    required   pam_loginuid.so' /etc/pam.d/crond
RUN echo "* * * * * /bin/echo 'it works!' >> /root/test.log" >> /var/spool/cron/root
RUN touch /var/log/cron.log
CMD crond && tail -f /var/log/cron.log
```