from django.conf.urls import patterns, include, url
from auth.views import *

urlpatterns = patterns('',

                       url(r'^register/$', 'auth.views.register', name='register'),  # ADD NEW PATTERN!
                       )
