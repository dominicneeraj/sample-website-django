import os
from django.db import models
from django.db.models.fields.related import OneToOneField
from django.conf import settings
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    country = models.CharField(max_length = 100, blank=False)


    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username