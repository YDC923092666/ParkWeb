#!/bin/bash

basepath=$(cd `dirname $0`; pwd)

function stop_uwsgi(){
kill -9 $(ps -ef |grep "${basepath}/django_socket.ini"  |grep -v grep |awk '{print $2}')
}


function start_uwsgi(){
   uwsgi -i ${basepath}/django_socket.ini
}


function restart(){
    stop_uwsgi
    sleep 5
    start_uwsgi

}
case $1 in 
    start)
        start_uwsgi
        ;;
    stop)
        stop_uwsgi 
        ;;
    restart)
        restart 
        ;;
    *)
        echo "bash `basename $0` start|stop|restart"
    ;;
esac
