#!/bin/bash
#
# usage
# $ tmux new-session  {this script}
#

BASE_DIR=$(cd $(dirname $0)/..; pwd)
BIN_DIR=$BASE_DIR/bin
APP_DIR=$BASE_DIR/app
RES_DIR=$BASE_DIR/res
HELP_DIR=$RES_DIR/help
CONF_DIR=$BASE_DIR/conf

. $CONF_DIR/conf

tmux unbind-key -a
tmux set-option -g mouse off
tmux set-option -g status-position top
tmux set-option -g status-interval 1
tmux set-option -g status-bg "colour57"
tmux set-option -g status-fg "colour255"
tmux set-option -g status-left-length 30
tmux set-option -g status-left "$TITLE  "
tmux set-window-option -g window-status-current-format " "
tmux set-option -g status-right "%m/%d %H:%M:%S#[default]"
tmux set -g pane-active-border-style "bg=default fg=cyan"

tmux set -g pane-border-status top
tmux split-pane -v -t 0
tmux split-pane -h -t 0
tmux split-pane -h -t 1
tmux split-pane -h -t 3

tmux resize-pane -x 40 -t 2
tmux resize-pane -y 20 -t 3

tmux select-pane -t 0 -T main
tmux select-pane -t 1 -T HELP
tmux select-pane -t 2 -T "I/O Stat"
tmux select-pane -t 3 -T eth0
tmux select-pane -t 4 -T eth1

tmux send-keys -t 1  "PS1=''" C-m
tmux send-keys -t 1  "$BIN_DIR/help.sh" C-m
tmux send-keys -t 2  "dstat -t --net -N eth0,eth1" C-m
tmux send-keys -t 3  "LANG=C sudo -E iftop -i eth0 -n" C-m
tmux send-keys -t 4  "LANG=C sudo -E iftop -i eth1 -n" C-m

# --- MAIN ---
tmux select-pane -t 0
$BIN_DIR/menu.sh

# --- END ---
tmux send-keys -t 1  C-c
tmux send-keys -t 3  C-c
tmux send-keys -t 4  C-c

tmux kill-pane -t 3
tmux kill-pane -t 2

tmux kill-server
