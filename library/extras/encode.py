
from threading import Thread, RLock
from time import sleep

# To serialize encoding process
lock = RLock()

class Encode(Thread):
    
    def __init__(self, obj):
        super(Encode, self).__init__()
        self.obj = obj

    def run(self):
        for i in range(20):
            with lock:
                print i
                sleep(1)
