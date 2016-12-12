from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone


class Contact(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    nick_name = models.CharField(max_length = 50)
    mail = models.EmailField('Email') 
    phone_number = models.CharField(max_length = 10)
    notes = models.CharField(max_length = 500)

    def __str__(self):
        return self.nick_name


class Stripe(models.Model):
    level =  models.IntegerField()
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name


class Event(models.Model):
    type_event =  models.ForeignKey(Stripe, on_delete=models.CASCADE)
    describe_event =  models.CharField(max_length = 500)
    start_time = models.DateTimeField('start event')
    limit = models.DateTimeField('Time long')
    importance = models.IntegerField(default=0) # Default?
    status = models.BooleanField(default=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s'%(self.type_event, self.start_time)



