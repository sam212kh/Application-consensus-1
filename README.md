# Application-consensus
Application designed to make screening school application quicker.

## Basic description and structure
School accounts
- Application school years/seasons/batch for example 18-19 for the 2018 - 2019 school year. Batches have a status or acrive or not.
- A list of applicants for the school season

School Staff
- each staff can see and review(rate) all appplication for active batches
- Staff are automaticly assigned a set number of students to review. _Need a setting the school season setup._

Applications
- each application gets reviewed by atleast the number of staff set in the season setting.
- the average review is calculated.

Dev server
http://dev.application.heteroskedastic.com


## steps to run local backend

1. pip install -r requirements.txt
1. cd consensus
1. python manage.py migrate --settings=consensus.settings.base
1. python manage.py createsuperuser --settings=consensus.settings.base # create superuser to login
1. python manage.py runserver --settings=consensus.settings.base


## steps to run local frontend
1. cd consensus/FRONTEND/consensus-ui
1. sudo npm install -g @vue/cli # (skip this if you installed once)
1. npm install # (skip this if you installed once)
1. npm run serve

