from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text