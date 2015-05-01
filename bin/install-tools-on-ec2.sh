#! /bin/bash

PJHOME=/home/ubuntu/django-ec2-template/
cd $PJHOME

sudo apt-get install mysql-server 
sudo apt-get install libmysqlclient-dev
sudo update-rc.d mysql defaults # Start MySQL on reboot
sudo apt-get install libpq-dev python-dev
pip install -r requirements.txt --allow-all-external

wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh

sudo apt-get install nginx
#sudo nginx -t
sudo service nginx start   # to start the server
#sudo service nginx status  # to poll for current status
#sudo service nginx stop    # to stop any servers if any
sudo update-rc.d -f nginx defaults
#sudo update-rc.d -f nginx remove
#bin/setup-nginx.sh

sudo pip install gunicorn
#bin/start-gnicorn.sh
