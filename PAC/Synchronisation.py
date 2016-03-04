import threading

class Synchronisation :
    def __init__(self):
        self.lock = threading._RLock()

    def synchronised(self,method):
        def f(*args):
            self.lock.acquire()
            try:
                return method(args)
            finally:
                self.lock.release()
        return f
