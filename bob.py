"""
Bob main class
@author: anguyen32
@version:1.0
"""
import sys
import subprocess
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

    def execute(self, command):
        # exec(open(self.command).read())
        file, args = command.split('--')
        file = file.strip(' ')
        args = " ".join("".join(args.split(' ')).split('-'))
        subprocess.call(['python3 {} {}'.format(file, args)],shell=True)

    def open(self):
        now = dt.now().time()
        return self.startTime < now < self.endTime

    def run(self):
        if self.open():
            log.info("running {}".format(self.command))
            if '--' in self.command:
                file, args = self.command.split('--')
                file = file.strip(' ')
                args = " ".join("".join(args.split(' ')).split('-'))
                # exec(open(self.command).read())
                subprocess.call(['python3 {} {}'.format(file, args)],shell = True)
            else:
                file = self.command
                subprocess.call(['python3 {}'.format(file)],shell=True)


# TODO : bob extendable by thread

if __name__ == "__main__":
    bob = Bob()
    script = "job/greet.py--"
    # script = "job/greet.py --  -args0   -args1    -args2"
    bob.execute(script)
