local -> [localhost:5000](localhost:5000)

```
$ heroku create
$ heroku config:add BUILDPACK_URL=git://github.com/heroku/heroku-buildpack-python.git

$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt --allow-all-external

$ python manage.py syncdb
$ foreman start web
```

remote

```
$ git push origin master
$ git push heroku master

$ heroku ps:scale web=1
$ heroku ps // how many dynos are running
$ heroku logs --tail

$ heroku run python manage.py syncdb
$ heroku open
```


