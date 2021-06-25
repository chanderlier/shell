有时候服务器上默认安装的git版本过低，fatal: git fetch-pack: expected shallow list

需要更新。
1.卸载git旧版本

yum remove git
2.安装依赖包

yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel asciidoc
yum install  gcc perl-ExtUtils-MakeMaker
3.编译安装最新的git版本

cd /usr/local/src/
wget -O git.zip https://github.com/git/git/archive/master.zip
unzip git.zip
cd git-master
make prefix=/usr/local/git all
make prefix=/usr/local/git install
4.添加到环境变量

echo "export PATH=$PATH:/usr/local/git/bin" >> ~/.bashrc
source ~/.bashrc

5.git最新版本更新完成

git --version