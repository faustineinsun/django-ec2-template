#! /bin/bash

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-pip

PJHOME=/home/ubuntu/Facebook-Graph/
cd $PJHOME

sudo pip install virtualenv
virtualenv venv
source venv/bin/activate

