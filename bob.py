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
        pass
    
    def run(self, job):
        exec(open(job).read())


if __name__ == "__main__":
    bob = Bob()
    print(log)
    script = 'job/greet.py'
    log.info("running {}".format(script))
    bob.run(script)
