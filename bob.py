'''
Bob main class
@author: anguyen32
@version:1.0
'''
import sys 
from logger.logger import Logger
log = Logger()

class Bob(object):
    def __init__(self):
        self.__name__ = "Bob"
        self.log = Logger(self.__name__)


    def execute(self, job):
        bob.log.info("running {}".format(job))
        exec(open(job).read())
# TODO : bob extendable by thread

if __name__ == "__main__":
    bob = Bob()
    script = 'job/greet.py'
    bob.execute(script)
