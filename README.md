local -> [localhost:5000](localhost:5000)

```
$ heroku create
$ heroku config:add BUILDPACK_URL=git://github.com/heroku/heroku-buildpack-python.git

>$ virtualenv venv
>$ source venv/bin/activate
$ pip install -r requirements.txt --allow-all-external
$ django-admin.py startproject polls // create a project called `polls`
>$ python manage.py syncdb   // Superuser -> Username:*u  Email: j@g Pswd:
>$ python manage.py runserver  // similar to `$ foreman start web`
>$ foreman start web

MySQL
https://docs.djangoproject.com/en/1.7/intro/tutorial01/
>$ sudo /usr/local/mysql/support-files/mysql.server start
$ sudo /usr/local/mysql/support-files/mysql.server stop
$ sudo /usr/local/mysql/support-files/mysql.server restart
>$ mysql -u root -p   // console
$ python manage.py makemigrations polls 
$ python manage.py sqlmigrate polls 0001
$ python manage.py check
$ python manage.py migrate
$ vim mysite/settings.py  // to change DATABASES setup (refer to https://devcenter.heroku.com/articles/cleardb)
$ heroku config -s | grep DATABASE_URL >> .env
>$ bin/beforeCommit.sh // backup `.env`

Django
>$ python manage.py shell  // console

config vars
$ vim .env
```

remote

```
>add, commit, and push
>$ git push origin master
>$ git push heroku master

$ heroku ps:scale web=1
$ heroku ps // how many dynos are running
$ heroku logs --tail

$ heroku addons:add papertrail
$ heroku addons
$ heroku addons:open papertrail

config vars
>$ heroku config:set TIMES=2
$ heroku config

MySQL
>$ heroku addons:open cleardb
$ heroku config:set MYSQL_INFO

>$ heroku run python manage.py shell   //console
>$ heroku run bash     // shell on that dyno
>$ heroku run python manage.py syncdb
>$ heroku open
```

