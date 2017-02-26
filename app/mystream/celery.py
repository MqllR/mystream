from __future__ import absolute_import
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mystream.settings')

app = Celery('mystream', 
            backend='amqp://'+os.environ['RABBIT_USER']+':'+os.environ['RABBIT_PASSWD']+'@'+os.environ['RABBIT_PORT_5672_TCP_ADDR']+':'+os.environ['RABBIT_PORT_5672_TCP_PORT']+'//',
            broker='amqp://'+os.environ['RABBIT_USER']+':'+os.environ['RABBIT_PASSWD']+'@'+os.environ['RABBIT_PORT_5672_TCP_ADDR']+':'+os.environ['RABBIT_PORT_5672_TCP_PORT']+'//',
        )
