local -> [localhost:5000](localhost:5000)

```
$ heroku create
$ heroku config:add BUILDPACK_URL=git://github.com/heroku/heroku-buildpack-python.git

$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt --allow-all-external
$ python manage.py syncdb
$ foreman start web

config vars
$ vim .env
```

remote

```
add, commit, and push
$ git push origin master
$ git push heroku master

$ heroku ps:scale web=1
$ heroku ps // how many dynos are running
$ heroku logs --tail

$ heroku addons:add papertrail
$ heroku addons
$ heroku addons:open papertrail

config vars
$ heroku config:set TIMES=2
$ heroku config

$ heroku run python manage.py shell   //console
$ heroku run bash     // shell on that dyno
$ heroku run python manage.py syncdb
$ heroku open
```
