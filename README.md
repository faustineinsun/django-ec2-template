local

```
$ heroku create
$ heroku config:add BUILDPACK_URL=git://github.com/heroku/heroku-buildpack-python.git
$ pip install -r requirements.txt
$ python manage.py syncdb
$ foreman start web
```

remote

```
$ git push origin master
$ git push heroku master
$ heroku ps:scale web=1
$ heroku run python manage.py syncdb
$ heroku open
```


