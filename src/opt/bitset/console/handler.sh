function menu_help(){
  cat $CONSOLE_DIR/help.txt
}

function menu_monitor(){
  sudo iftop -i $1
  clear
}

function menu_clear(){
  filter_init
}

function menu_delay(){
  arg1=""
  arg2=""
  if [ -z "$1" ]; then
    echo "[usage] delay  {delay}  {diff}"
  else
    arg1=$1ms

    if [ -n "$2" ]; then
      arg2=$2ms
    fi
    filter_delay $arg1 $arg2
  fi
}

function menu_loss(){
  arg1=""
  if [ -z "$1" ]; then
    echo "[usage] loss  {loss}"
  else
    arg1="$1%"

    filter_loss $arg1
  fi
}


