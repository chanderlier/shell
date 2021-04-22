从已有代码的目录上传代码到远程git仓库
git init //生成.git目录
gitk  add . //把当前目录里的文件加入到暂存区
git commit -m '上传' //从暂存区提交到仓库
git remote add origin 远程仓库地址 //添加远程仓库
git branch --set-upstream-to=origin/<branch> master //本地仓库和远程仓库关联，git pull时就会有提示
git status //会有信息显示:Your branch is up-to-date with 'origin/master'.
不过一般远程仓库会和现有仓库合并不了，单纯的git pull会提示fatal: refusing to merge unrelated histories
git pull --rebase origin master //看来以rebase变基的方式可以合并啊
git push	 //提交到远程仓库

上传前端代码到frontend分支
git init 
git remote add frontend  远程仓库地址
git  checkout -b frontend
git add .
git commit -m 'message'
git push frontend frontend 

git clone -b uat 远程仓库
拉取远程仓库uat分支的代码


从已有的代码目录更新代码
```sh
ls 
```
```sh
Dockerfile README.md  k8s        nginx      src        start.sh
```
更新src里面的代码

```sh
git add .
```
```sh
git commit -m 'update'
```
```sh
git push frontend frontend
```

## git 回滚
代码回滚
在上传代码到远程仓库的时候，不免会出现问题，任何过程都有可能要回滚代码：

1、在工作区的代码

git checkout -- a.txt   # 丢弃某个文件，或者
git checkout -- .       # 丢弃全部

2、代码git add到缓存区，并未commit提交

git reset HEAD .  或者
git reset HEAD a.txt


3、git commit到本地分支、但没有git push到远程

git log # 得到你需要回退一次提交的commit id
git reset --hard <commit_id>  # 回到其中你想要的某个版
或者
git reset --hard HEAD^  # 回到最新的一次提交
或者
git reset HEAD^  # 此时代码保留，回到 git add 之前

4、git push把修改提交到远程仓库
1）通过git reset是直接删除指定的commit

git log # 得到你需要回退一次提交的commit id
git reset --hard <commit_id>
git push origin HEAD -f # 强制提交一次，之前错误的提交就从远程仓库删除

2）通过git revert是用一次新的commit来回滚之前的commit

git log # 得到你需要回退一次提交的commit id
git revert <commit_id>  # 撤销指定的版本，撤销也会作为一次提交进行保存
