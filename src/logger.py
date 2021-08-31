import sys


class Logger(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._debug = False
            cls._inform = False
        return cls._instance

    def set_debug(self, val):
        self._debug = val

    def set_inform(self, val):
        self._inform = val

    def log_debug(self, *args, **kwargs):
        if self._debug:
            print(*args, **kwargs)

    def log_inform(self, *args, **kwargs):
        if self._inform:
            print(*args, **kwargs)

    def log_error(self, *args, **kwargs):
        print(*args, **kwargs, file=sys.stderr)
