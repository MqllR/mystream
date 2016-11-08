from __future__ import absolute_import
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mystream.settings')

app = Celery('mystream', 
            backend='amqp://guest:guest@localhost:5672//',
            broker='amqp://guest:guest@localhost:5672//'
        )
