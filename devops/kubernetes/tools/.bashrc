# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
alias c='clear'
alias kcf='kubectl create -f'
alias kdf='kubectl delete -f'
alias kgp='kubectl get pod'
alias kdp='kubectl describe pod'

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi