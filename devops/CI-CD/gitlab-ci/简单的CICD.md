代码提交到gitlab，自动触发部署到目标服务器上的指定目录下。
开发服务器|gitlab服务器|测试服务器|
|  ----  | ----  | ---- | 
| 192.168.10.123 | 10.0.10.177 |10.0.10.177 |




```yaml
# 默认环境变量
# $CI_PROJECT_NAME: 仓库名
# $CI_PROJECT_DIR: 项目绝对目录
# $CI_PROJECT_URL: 仓库地址
# $CI_COMMIT_REF_NAME: 提交的分支名
# $GITLAB_USER_EMAIL: 用户邮箱

variables:
  DOMAIN: dieser.com
  PROD_DOMAIN: douyin
  REMOTE_IP: 10.0.10.177
  PROJECT_PATH: /data/server/
  UTILS_PATH: /alidata/server/runner/utils
  HOME: /home/gitlab-runner/.ssh


stages:
  - PullCode
  - ConfirmRun
  - SyncProject
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
  tags:
    - drunner

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
  tags:
    - drunner

ConfirmOperation:
  stage: ConfirmRun
  script: 
    - echo "operation must be confirm"
  only:
    - product
  tags:
    - drunner
  when: manual
  allow_failure: false



SyncCode:
  stage: SyncProject
  script:
    - |
      echo "Sync project dir to remote host"
      for host in $REMOTE_IP; do
        echo "rsync -avzP -e "ssh -i ${HOME}/id_rsa -o 'StrictHostKeyChecking no'" $CI_PROJECT_DIR/* root@$host:$PROJECT_PATH/"
        rsync -avzP  -e "ssh -i ${HOME}/id_rsa -o 'StrictHostKeyChecking no'"  $CI_PROJECT_DIR/* root@$host:$PROJECT_PATH/
      done
  only:
    - product
  tags:
    - drunner

SuccessSendMSG:
  stage: SendMSG
  script:
    - /usr/bin/python $UTILS_PATH/sendmsg_utils.py '成功' $CI_COMMIT_REF_NAME $PROD_DOMAIN $PROD_DOMAIN.$DOMAIN $GITLAB_USER_EMAIL $CI_PROJECT_URL 'None' 'dqyapi'
  only:
    - product
  tags:
    - drunner
  when: on_success

FailedSendMSG:
  stage: SendMSG
  script:
    - /usr/bin/python $UTILS_PATH/sendmsg_utils.py '失败' $CI_COMMIT_REF_NAME $PROD_DOMAIN $PROD_DOMAIN.$DOMAIN $GITLAB_USER_EMAIL $CI_PROJECT_URL 'None' 'dqyapi'
  only:
    - product
  tags:
    - drunner
  when: on_failure
```