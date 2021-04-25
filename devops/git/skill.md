### 常用命令
git init #生成.git目录
gitk  add . #把当前目录里的文件加入到暂存区
git checkout branch #切换分支
git switch branch #切换分支
git checkout -b dev #创建并切换到dev分支
git switch -c dev #创建并切换到dev分支
git merge dev #合并dev分支到当前分支
git branch -d dev #删除dev分支
git commit -m '上传' #从暂存区提交到仓库
git remote add origin 远程仓库地址 #添加远程仓库
git branch --set-upstream-to=origin/<branch> master #本地仓库和远程仓库关联，git pull时就会有提示
git status #会有信息显示:Your branch is up-to-date with 'origin/master'.
不过一般远程仓库会和现有仓库合并不了，单纯的git pull会提示fatal: refusing to merge unrelated histories
git pull --rebase origin master #看来以rebase变基的方式可以合并啊
git push	 #提交到远程仓库
git clone -b uat 远程仓库 #拉取远程仓库uat分支的代码
git status #查看状态
git stash #储存当前工作目录
git stash list
git stash apply
git stash drop
git stash pop
git cherry-pick commitid #复制一个特定的提交到当前分支
### 代码同步
上传前端代码到frontend分支
git init #初始化当前目录
git remote add frontend  远程仓库地址 #添加远程仓库地址
git  checkout -b frontend  #在本地创建frontend分支并切换到该分支
git add .
git commit -m 'message'
git push frontend frontend 


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

###  git 回滚
代码回滚
在上传代码到远程仓库的时候，不免会出现问题，任何过程都有可能要回滚代码：

1、在工作区的代码

git checkout -- a.txt   #丢弃某个文件，或者
git checkout -- .       #丢弃全部

2、代码git add到缓存区，并未commit提交

git reset HEAD .  或者
git reset HEAD a.txt


3、git commit到本地分支、但没有git push到远程。在提交git commit时，message最好能够详细的记录这次提交的信息，以便后续任何情况需要回滚时，能快速确定id。

git log #得到你需要回退一次提交的commit id
git reset --hard <commit_id>  #回到其中你想要的某个版
或者
git reset --hard HEAD^  #回到最新的一次提交
git reset --hard HEAD^^ #回到上上个版本
git reset --hard HEAD-10 #回到十个版本之前
或者
git reset HEAD^  #此时代码保留，回到 git add 之前

4、git push把修改提交到远程仓库
1）通过git reset是直接删除指定的commit

git log #得到你需要回退一次提交的commit id
git reset --hard <commit_id>
git push origin HEAD -f #强制提交一次，之前错误的提交就从远程仓库删除

2）通过git revert是用一次新的commit来回滚之前的commit

git log #得到你需要回退一次提交的commit id
git revert <commit_id>  #撤销指定的版本，撤销也会作为一次提交进行保存
