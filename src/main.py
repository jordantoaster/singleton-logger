from logger import Logger
from dummy_class import Dummy

logger = Logger()
# logger = Logger() - does not create a new logger, print is not repeated.

def main():
    dummy = Dummy("Bard")
    dummy.do_something()

if __name__ == "__main__":
    main()
    print('done')