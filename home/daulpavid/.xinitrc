#!/bin/sh

urxvt=$HOME/.urxvtrc
terminalcolors=$HOME/.terminalcolors

if [ -f $urxvt ]; then
    xrdb -merge $urxvt
fi

if [ -f $terminalcolors ]; then
    xrdb -merge $terminalcolors
fi

exec qtile
