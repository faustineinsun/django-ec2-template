from django.db import models

# Create your models here.

# from https://docs.djangoproject.com/en/1.7/intro/tutorial01/
import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    # to string
    #def __str__(self):          # Python 3     
    #    return self.question_text
    def __str__(self):          # __unicode__ on Python 2
        if hasattr(self, '__unicode__'):
            return unicode(self.question_text).encode('utf-8')
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # to string
    #def __str__(self):          # Python 3     
    #    return self.choice_text
    def __str__(self):          # __unicode__ on Python 2
        if hasattr(self, '__unicode__'):
            return unicode(self.choice_text).encode('utf-8')
        return self.choice_text

class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
