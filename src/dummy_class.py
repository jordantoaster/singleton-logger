from logger import Logger

logger = Logger()

class Dummy:

    def __init__(self, name):
        self.name = name

    def do_something(self):
        print("I'm a dummy class, I don't do anything.")
        logger.log('log')