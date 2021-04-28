新建一个项目
添加.gitlab-ci.yml
```yaml
stages:
  - build
  - test
  - deploy

build-job:
  stage: build
  script:
    - echo "Hello, $GITLAB_USER_LOGIN!"
  tags:
    - test

test-job1:
  stage: test
  script:
    - echo "This job tests something"
  tags:
    - test
    
test-job2:
  stage: test
  script:
    - echo "This job tests something, but takes more time than test-job1."
    - echo "After the echo commands complete, it runs the sleep command for 20 seconds"
    - echo "which simulates a test that runs 20 seconds longer than test-job1"
    - sleep 20
  tags:
    - test

deploy-prod:
  stage: deploy
  script:
    - echo "This job deploys something from the $CI_COMMIT_BRANCH branch."
  tags:
    - test

```
此处tags 对应的是gitlab-runner的tag，需要为字符串。如果不写会报错。