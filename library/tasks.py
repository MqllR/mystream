from celery import task

from .extras.encode import Encode

@task()
def encode_stream(streamtmp):
    enc = Encode(streamtmp)
    enc.run()

    return None
