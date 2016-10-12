from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone


class Contact(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    nick_name = models.CharField(max_length = 50)
    mail = models.IntegerField() 
    phone_number = models.IntegerField() 
    notes = models.CharField(max_length = 500)

    def __str__(self):
        return (self.nick_name, self.phone_number)


class Event(models.Model):
    type_event = models.CharField(max_length = 50)
    some_event =  models.CharField(max_length = 500)
    start_time = models.DateTimeField('date published')
    limit = models.DateTimeField('date published')
    importance = models.IntegerField(default=0) # Default?
    status = models.BooleanField(default=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return (self.type_event, self.start_time)


class Types(models.Model):
    level =  models.IntegerField()
    name = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return (self.level, self.name)


