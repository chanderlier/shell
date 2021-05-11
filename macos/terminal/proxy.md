当前mac用的是zsh
```sg
vim ~/.zshrc
```
添加下面两行
```sh
alias proxy='export all_proxy=socks5://127.0.0.1:1086'
alias unproxy='unset all_proxy'
```
```sh
source ~/.zshrc
```