#! /bin/bash
sudo apt-get update | sudo apt-get upgrade
sudo apt-get install python-pip
sudo pip install virtualenv

PJHOME=/home/ubuntu/Facebook-Graph/
cd $PJHOME
virtualenv venv
source venv/bin/activate
sudo apt-get install mysql-server 
sudo apt-get install libmysqlclient-dev
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
$PJHOME`bin/setup-nginx.sh`

sudo pip install gunicorn
$PJHOME`bin/start-gnicorn.sh`
