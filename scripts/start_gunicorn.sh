#!/bin/bash

NAME="istkicklschonweg.at"                            # Name of the application (*)
DJANGODIR=/srv/istkicklschonweg.at                    # Django project directory (*)
SOCKFILE=$DJANGODIR/run/gunicorn.sock                 # we will communicate using this unix socket (*)
ACCESS_LOGFILE=$DJANGODIR/logs/gunicorn-access.log
ERROR_LOGFILE=$DJANGODIR/logs/gunicorn-error.log
VIRTUALENV=$DJANGODIR/.env
USER=www-data                                         # the user to run as (*)
GROUP=www-data                                        # the group to run as (*)
NUM_WORKERS=1                                         # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=settings.prod           # which settings file should Django use (*)
DJANGO_WSGI_MODULE=wsgi                        # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source "$VIRTUALENV/bin/activate"
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec $VIRTUALENV/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --error-logfile $ERROR_LOGFILE \
  --access-logfile $ACCESS_LOGFILE \
  --bind=unix:$SOCKFILE
