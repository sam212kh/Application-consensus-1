#!/bin/bash

BRANCH=master
if [ -n "$1" ]; then
    BRANCH=$1
fi

NAME="consensus"
GITURL=https://github.com/vincentdavis/Application-consensus.git
ROOTDIR=/opt/webapps
PROJECTDIR=${ROOTDIR}/${NAME}
DJANGODIR=${PROJECTDIR}/${NAME}
ENVDIR=${PROJECTDIR}/env
DJANGO_SETTINGS_MODULE=consensus.settings.main

echo "+++ Deploying $NAME: BRANCH=$BRANCH PROJECTDIR=$PROJECTDIR ..."

mkdir -p ${PROJECTDIR}
mkdir -p ${PROJECTDIR}/run
mkdir -p ${PROJECTDIR}/logs
mkdir -p ${PROJECTDIR}/etc
mkdir -p ${PROJECTDIR}/tmp

if [ -d "$DJANGODIR" ]; then
    cd ${DJANGODIR}
    git reset --hard HEAD
    git pull origin --recurse-submodules
    git checkout ${BRANCH}
    git pull --recurse-submodules
else
    git clone ${GITURL} -b ${BRANCH} ${DJANGODIR}
fi
sudo supervisorctl stop ${NAME}
#sudo supervisorctl stop ${NAME}-celerybeat
#sudo supervisorctl stop ${NAME}-celeryworker
sleep 1
if [ ! -d "$ENVDIR" ]; then
    virtualenv -p python3 ${ENVDIR}
fi
source ${ENVDIR}/bin/activate
cd ${DJANGODIR}
pip install -r requirements.txt
pip install django-gunicorn
cd $DJANGODIR/consensus
python manage.py migrate --settings=${DJANGO_SETTINGS_MODULE} --noinput
python manage.py collectstatic --settings=${DJANGO_SETTINGS_MODULE} --noinput
sudo supervisorctl start ${NAME}
#sudo supervisorctl start ${NAME}-celerybeat
#sudo supervisorctl start ${NAME}-celeryworker
sudo service supervisor restart
sudo service nginx restart

echo
echo "Finished!"
