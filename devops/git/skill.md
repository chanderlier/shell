igit init //生成.git目录
gitkki add . //把当前目录里的文件加入到暂存区
git commit -m '上传' //从暂存区提交到仓库
git remote add origin 远程仓库地址 //添加远程仓库
git branch --set-upstream-to=origin/<branch> master //本地仓库和远程仓库关联，git pull时就会有提示
git status //会有信息显示:Your branch is up-to-date with 'origin/master'.
不过一般远程仓库会和现有仓库合并不了，单纯的git pull会提示fatal: refusing to merge unrelated histories
git pull --rebase origin master //看来以rebase变基的方式可以合并啊
git push	 //提交到远程仓库