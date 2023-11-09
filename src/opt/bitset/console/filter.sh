function check_bridge(){
  brctl show $BRIDGE > /dev/null
  return $?
}

function filter_add(){
  sudo tc qdisc add dev $DEV root netem 
}


function filter_init(){
  sudo tc qdisc del dev $DEV root  
  sudo tc qdisc add dev $DEV root netem 
}

function filter_delay(){
  sudo tc qdisc change dev $DEV root netem delay $1 $2 
}

function filter_loss(){
  sudo tc qdisc change dev $DEV root netem loss $1
}
