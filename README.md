### Deploying a django app on ec2

#### 1. Setup Gitbub

* [Github Generating SSH keys](https://help.github.com/articles/generating-ssh-keys/)

```
$ sudo apt-get install git
$ git config --global user.name "Your Name"
$ git config --global user.email "your@email.com"
```
	
#### 2. Install tools

```
$ git clone https://github.com/faustineinsun/Facebook-Graph.git
$ cd Facebook-Graph
modify bin/django-nginx-config, change `ec2-x-x-x-x.compute-1.amazonaws.com`
$ bin/setup-virtualenv.sh
$ source venv/bin/activate
$ bin/install-tools-on-ec2.sh
```

#### 3. MySQL

```
$ sudo service mysql restart
$ sudo service mysql status
$ mysql -u root -p  // console
mysql> CREATE DATABASE django_deploy;
mysql> SHOW DATABASES;

$ vim ~/.profile
>> export MYSQL_PSWRD=***
$ source ~/.profile
$ source venv/bin/activate

$ python manage.py shell
follow `Playing with the API` section in https://docs.djangoproject.com/en/1.7/intro/tutorial01/ and add records into database

$ python manage.py makemigrations polls 
$ python manage.py sqlmigrate polls 0001
$ python manage.py sqlmigrate polls 0002
$ python manage.py check
--$ python manage.py migrate
$ python manage.py syncdb   // Superuser -> Username: ubuntu  Email: f@g Pswd:
```

#### 4. Start gnicorn and nginx

```
$ bin/start-gnicorn.sh
$ bin/setup-nginx.sh
```

### Django

```
--$ django-admin.py startproject polls // create a project called `polls`
$ python manage.py shell  // console
```

