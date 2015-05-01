# http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/

#sudo vim /etc/nginx/nginx.conf
#sudo vim /etc/nginx/sites-enabled/default

PJHOME=/home/ubuntu/django-ec2-template/
FNAME=django-nginx-config
sudo cp $PJHOME'bin/'$FNAME /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/$FNAME /etc/nginx/sites-enabled/$FNAME
sudo service nginx restart
