#!/bin/bash
PJNAME=Facebook-Graph
APPNAME=mysite

PJDIR=/home/ubuntu/$PJNAME/
APPDIR=$PJDIR$APPNAME/

LOGFILE=$PJDIR'log/gunicorn.log'
ERRORFILE=$PJDIR'log/gunicorn-error.log'

NUM_WORKERS=3

ADDRESS=127.0.0.1:8000

source ~/.bashrc

cd $PJDIR
if [ ! -d "log" ]; then
	mkdir log
fi

# netstat -tulpn
# kill xx

exec gunicorn $APPNAME.wsgi:application -w $NUM_WORKERS --bind=$ADDRESS --log-level=debug --log-file=$LOGFILE 2>>$LOGFILE  1>>$ERRORFILE &
