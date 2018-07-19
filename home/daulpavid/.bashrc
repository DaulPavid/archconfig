#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export VISUAL=vim
export EDITOR="$VISUAL"

set -o vi
