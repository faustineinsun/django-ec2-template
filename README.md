#### EC2

* [website](http://ec2-52-4-105-143.compute-1.amazonaws.com/)
	* [Github Generating SSH keys](https://help.github.com/articles/generating-ssh-keys/)
		* $ git config --global user.name "Your Name"
		* $ git config --global user.email "your@email.com"
	
```
modify bin/django-nginx-config, change `ec2-x-x-x-x.compute-1.amazonaws.com/`
$ bin/install-virtualenv.sh
$ source venv/bin/activate
$ bin/install-tools-on-ec2.sh
$ bin/setup-nginx.sh
```

#### MySQL

```
$ sudo service mysql restart
$ sudo service mysql status
$ mysql -u root -p  // console
mysql> CREATE DATABASE django_deploy;
mysql> SHOW DATABASES;

https://docs.djangoproject.com/en/1.7/intro/tutorial01/
$ python manage.py makemigrations polls 
$ python manage.py sqlmigrate polls 0001
$ python manage.py check
$ python manage.py migrate
$ python manage.py syncdb   // Superuser -> Username: ubuntu  Email: f@g Pswd:
```

#### Django

```
$ django-admin.py startproject polls // create a project called `polls`
$ python manage.py shell  // console
```

