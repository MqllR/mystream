from celery import task

from .extras.encode import Encode

@task()
def encode_stream(streamtmp, quality):
    enc = Encode(streamtmp, quality)
    enc.run()

@task()
def post_encoding(streamtmp):
    enc = Encode(streamtmp)
    enc.post_encoding()
