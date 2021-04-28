现在有测试服务器10.0.10.168,正式服务器10.0.10.199 gitlab服务器10.0.10.177 本地开发10.0.10.188
本地提交代码到gitlab，自动触发cicd流程，将代码部署到测试服务器上。
现在项目下有develop分支和product分支，要求develop分支下的代码变更触发自动部署，product下需要手动确认才触发部署。部署结果通过邮件通知到指定邮箱上。
准备工作,在gitlab-runner服务器上生成密钥
su gitlab-runner
```sh
ssh-keygen -t RSA 
```
一直回车
将id_rsa.pub分别添加到测试服务器和正式服务器的www用户下authorized_keys中
ssh www@10.0.10.168 'cat /home/gitlab-runner/.ssh/id_rsa.pub >> /home/www/.ssh/authorized_keys'

```yaml
variables:
    DOMAIN: dieser.cn
    DEV_DOMAIN: dev
    PROD_DOMAIN: prd
    TAR_PATH: '*'
    EXCLUDE_PATH: '{README.md}'
    DEV_HOSTS: 10.0.10.168
    PROD_HOSTS: 10.0.10.199
    NGINX_PATH: /etc/nginx/conf.d/vhosts
    UTILS_PATH: /data/gitlab-runner/utils
    REMOTE_NGINX_PATH: /home/dev/nginx/vhosts 
    DEV_PROJECT_PATH: /data/www


stages：
  - PullCode
  - IsProduct
  - Build
  - ReloadNginx
  - SetDomain
  - SendMSG


EchoBuildInfo:
  stage: PullCode
  script: 
    - echo "$CI_PROJECT_URL"
    - echo "$GITLAB_USER_EMAIL"
    - echo "$GITLAB_USER_LOGIN"
    - echo "$GITLAB_USER_NAME"
    - echo "$DOMAIN"
    - echo "$DEV_DOMAIN.$DOMAIN"
    - echo "$PROD_DOMAIN.$DOMAIN"
    - export
  only:
    - product
    - develop
  tags:
    - test

IsBelongItself:
  stage: PullCode
  script: 
    - |
      echo ".$PROD_DOMAIN.$DOMAIN"
      if [[ -f ".$PROD_DOMAIN.$DOMAIN" ]]; then
        echo "This project is belong to itself"
      else
        echo "Error this project is not belong to itself. please check."
        exit 1
      fi
  only:
    - product
    - develop
  tags:
    - test

WhenRunProduct:
  stage: IsProduct
  script: 
    - echo "product must be confirm"
  only:
    - product
  tags:
    - test
  when: manual
  allow_failure: false

ReleaseProject:
  stage: Build
  environment:
    name: DeployRecord
    url: https://$PROD_DOMAIN.$DOMAIN
  before_script:
    - |
      if [[ -e $CI_PROJECT_DIR ]]; then 
        echo "$CI_PROJECT_DIR is exist"
      else
        echo "$CI_PROJECT_DIR is not  exist"
        exit 1
      fi
  script:
    - echo "Sync project dir to remote host"
    - |
      if [[ $CI_COMMIT_REF_NAME == "product" ]]; then
        HOSTS=$PROD_HOSTS
        FULL_DOMAIN=$PROD_DOMAIN.$DOMAIN
        USER=www
      else
        HOSTS=$DEV_HOSTS
        FULL_DOMAIN=$DEV_DOMAIN.$DOMAIN
        USER=dev
      fi
      for host in $HOSTS; do
        echo "rsync -avzP --exclude=$EXCLUDE_PATH  $CI_PROJECT_DIR/$TAR_PATH $USER@$host:$DEV_PROJECT_PATH/$FULL_DOMAIN/"
        rsync -avzP --exclude=$EXCLUDE_PATH  $CI_PROJECT_DIR/$TAR_PATH $USER@$host:$DEV_PROJECT_PATH/$FULL_DOMAIN/
      done
  only:
    - product
    - develop
  tags:
    - test

AddNginxConf:
  stage: Build
  before_script:
    - |
      if [[ $CI_COMMIT_REF_NAME == "product" ]]; then
        FULL_DOMAIN=$PROD_DOMAIN.$DOMAIN
      else
        FULL_DOMAIN=$DEV_DOMAIN.$DOMAIN
      fi
      if [[ -f $NGINX_PATH/.$FULL_DOMAIN ]]; then echo "Not first release. Skip"; exit 0; fi
      cp -a $NGINX_PATH/backend_template.conf  $NGINX_PATH/$FULL_DOMAIN.conf
      sed -i  -e "s/FULL_DOMAIN/$FULL_DOMAIN/g"  -e "s/PHP_PORT/$PHP_PORT/g" $NGINX_PATH/$FULL_DOMAIN.conf
      cat  $NGINX_PATH/$FULL_DOMAIN.conf
  script:
    - |
      echo "Sync nginx config file to remote"
      if [[ $CI_COMMIT_REF_NAME == "product" ]]; then
        HOSTS=$PROD_HOSTS
        FULL_DOMAIN=$PROD_DOMAIN.$DOMAIN
        USER=www
        REMOTE_NGINX_PATH=/alidata/server/openresty/nginx/conf/vhosts
      else
        HOSTS=$DEV_HOSTS
        FULL_DOMAIN=$DEV_DOMAIN.$DOMAIN
        USER=dev
      fi
      if [[ -f $NGINX_PATH/.$FULL_DOMAIN ]]; then echo "Not first release. Skip"; exit 0; fi
      for host in $HOSTS; do
        echo "rsync -avzP $NGINX_PATH/$FULL_DOMAIN.conf $USER@$host:$REMOTE_NGINX_PATH/"
        rsync -avzP $NGINX_PATH/$FULL_DOMAIN.conf $USER@$host:$REMOTE_NGINX_PATH/
      done
  only:
    - product
    - develop
  tags:
    - test

NginxReload:
  stage: ReloadNginx
  script:
    - |
      echo "Reload remote nginx"
      if [[ $CI_COMMIT_REF_NAME == "product" ]]; then
        HOSTS=$PROD_HOSTS
        FULL_DOMAIN=$PROD_DOMAIN.$DOMAIN
        USER=www
      else
        HOSTS=$DEV_HOSTS
        FULL_DOMAIN=$DEV_DOMAIN.$DOMAIN
        USER=dev
      fi
      if [[ -f $NGINX_PATH/.$FULL_DOMAIN ]]; then echo "Not first release. Skip"; exit 0; fi
      for host in $HOSTS; do
        echo /usr/bin/ssh  $USER@$host "sudo $REMOTE_NGINX_BIN/nginx -t && sudo $REMOTE_NGINX_BIN/nginx -s reload"
        /usr/bin/ssh  $USER@$host "sudo $REMOTE_NGINX_BIN/nginx -t && sudo $REMOTE_NGINX_BIN/nginx -s reload"
      done
  only:
    - product
    - develop
  tags:
    - test

AddHostRecord:
  stage: SetDomain
  script:
    - |
      if [[ $CI_COMMIT_REF_NAME == "product" ]]; then
        FULL_DOMAIN=$PROD_DOMAIN.$DOMAIN
      else
        FULL_DOMAIN=$DEV_DOMAIN.$DOMAIN
      fi
    - echo "/usr/bin/python $UTILS_PATH/dnspod_utils.py $FULL_DOMAIN"
    - /usr/bin/python $UTILS_PATH/dnspod_utils.py $FULL_DOMAIN
  only:
    - product
    - develop
  tags:
    - test
  allow_failure: true

AddSlbRule:
  stage: SetDomain
  script:
    - echo "/usr/bin/python $UTILS_PATH/aliyun_slb_utils.py $PROD_DOMAIN.$DOMAIN"
    - /usr/bin/python $UTILS_PATH/aliyun_slb_utils.py $PROD_DOMAIN.$DOMAIN
  only:
    - product
  tags:
    - test
  allow_failure: true

SuccessSendMSG:
  stage: SendMSG
  script:
    - |
      if [[ $CI_COMMIT_REF_NAME == "product" ]]; then
        SUB_DOMAIN=$PROD_DOMAIN
      else
        SUB_DOMAIN=$DEV_DOMAIN
      fi
      if [[ ! -f $NGINX_PATH/.$SUB_DOMAIN.$DOMAIN ]]; then touch $NGINX_PATH/.$SUB_DOMAIN.$DOMAIN; fi
      /usr/bin/python $UTILS_PATH/sendmsg.py '成功' $CI_COMMIT_REF_NAME $SUB_DOMAIN $SUB_DOMAIN.$DOMAIN $GITLAB_USER_EMAIL $CI_PROJECT_URL 'None' 'bqyapi'
  only:
    - product
    - develop
  tags:
    - test
  when: on_success

FailedSendMSG:
  stage: SendMSG
  script:
    - |
      if [[ $CI_COMMIT_REF_NAME == "product" ]]; then
        SUB_DOMAIN=$PROD_DOMAIN
      else
        SUB_DOMAIN=$DEV_DOMAIN
      fi
      /usr/bin/python $UTILS_PATH/sendmsg.py '失败' $CI_COMMIT_REF_NAME $SUB_DOMAIN $SUB_DOMAIN.$DOMAIN $GITLAB_USER_EMAIL $CI_PROJECT_URL 'None' 'bqyapi'
  only:
    - product
    - develop
  tags:
    - test
  when: on_failure
  ```

