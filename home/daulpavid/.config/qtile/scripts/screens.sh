#!/bin/sh
#
# Current screen configuration for Qtile
#

sleep 1

xrandr --output HDMI-0 --primary --mode 2560x1080 --left-of DVI-D-0
xrandr --output DVI-D-0 --mode 1440x900 --right-of HDMI-0
xrandr --output DVI-D-0 --rotate left
