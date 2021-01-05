[innergit]
1.
docker exec -it 9753e902795a /bin/bash
2.
gitlab-rake gitlab:backup:create
3.
scp 1609749148_2021_01_04_13.2.1_gitlab_backup.tar  root@10.0.10.168:~
4.
scp /etc/gitlab/gitlab.rb  root@10.0.10.188:~
5.
scp /etc/gitlab/gitlab-secrets.json  root@10.0.10.188:~

[server]
6.
wget --content-disposition https://packages.gitlab.com/gitlab/gitlab-ce/packages/el/7/gitlab-ce-13.2.1-ce.0.el7.x86_64.rpm/download.rpm
7.
yum install -y policycoreutils-python
8.
rpm -ivh gitlab-ce-13.2.1-ce.0.el7.x86_64.rpm 
9.
mv gitlab.rb /etc/gitlab/gitlab.rb
mv gitlab-secrets.json /etc/gitlab/gitlab-secrets.json
10.
gitlab-ctl reconfigure
gitlab-ctl stop sidekiq
chmod 777 1609749148_2021_01_04_13.2.1_gitlab_backup.tar 
mv 1609749148_2021_01_04_13.2.1_gitlab_backup.tar  /var/opt/gitlab/backups/
cd /var/opt/gitlab/backups/
gitlab-rake gitlab:backup:restore BACKUP=1609749148_2021_01_04_13.2.1
