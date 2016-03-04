import threading


class Synchronisation:
    def __init__(self):
        self.lock = threading.RLock()

    @staticmethod
    def synchronised(method):
        def f(*args):
            self = args[0]
            self.lock.acquire()
            try:
                return method(*args)
            finally:
                self.lock.release()
        return f
