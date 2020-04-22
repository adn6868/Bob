"""
Bob main class
@author: anguyen32
@version:1.0
"""
import sys
from datetime import datetime as dt
from logger.logger import Logger

log = Logger()


class Bob(object):
    def __init__(self, jobDict=None):
        self.__name__ = "Bob"
        self.log = Logger(self.__name__)
        self.status = "OPEN"
        if jobDict:
            self.id = jobDict["id"]
            self.startTime = dt.strptime(jobDict["start"], "%H%M %Z").time()
            self.endTime = dt.strptime(jobDict["end"], "%H%M %Z").time()
            self.command = jobDict["command"]
            self.priority = jobDict["priority"]
            self.notify = jobDict["notify"]

    def execute(self, job):
        bob.log.info("running {}".format(job))
        exec(open(job).read())

    def open(self):
        now = dt.now().time()
        return self.startTime < now < self.endTime

    def run(self):
        if self.open():
            log.info("running {}".format(self.command))
            exec(open(self.command).read())
            #TODO: Allow args from sch file


# TODO : bob extendable by thread

if __name__ == "__main__":
    bob = Bob()
    script = "job/greet.py"
    bob.execute(script)
