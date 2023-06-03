import logging
import sys

class Logger(object):

    __instance = None
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    def __new__(cls):
        if not cls.__instance:
            print('creating new logger')
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def log(self, message, level=logging.INFO):
        logging.log(level, message)