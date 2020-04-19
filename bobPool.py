from bob import Bob
import os
import pprint as pp
from logger.logger import Logger
import queue as Q
import datetime as dt
from multiprocessing.dummy import Pool as ThreadPool

log = Logger()


class BobPool(object):
    def __init__(self, name="Bob Pool: Chicago 01"):
        self.__name__ = name
        self.jobDict = {}
        self.jobQueue = Q.PriorityQueue()
        self.log = Logger()

    def genJobDict(self, osPath="schedule"):  # TODO: Tokken handling this
        for root, dirs, files in os.walk(osPath):
            for file in files:
                with open(os.path.join(root, file), "r") as auto:
                    fileData = {}
                    for line in auto:
                        line = line.split(":")
                        fileData[line[0].strip(" ")] = "".join(line[1:]).strip("\n")
                    self.jobDict[auto.name] = fileData

    def getJobQueue(self):
        for job in self.jobDict:
            jobDetail = self.jobDict[job]
            print(jobDetail["start"])
            a = dt.datetime.strptime(jobDetail["start"], "%H%M GMT")
            print(a)
            timeStart = dt.datetime.strptime(jobDetail["start"], "%H%M GMT")
            self.jobQueue.put((timeStart, job))

    def _executeBob(self, job):
        self.log.info("Executing job {}".format(job))
        jobDefinition = self.jobDict[job]
        self.log.info("jobDefinition: {}".format(jobDefinition))
        # TODO: allow Bob.py to read job Definition

    def executeBob(self):
        if not self.jobDict:
            self.genJobDict()
            self.getJobQueue()
        self.pool = ThreadPool(len(self.jobDict))
        stdout = self.pool.map(self._executeBob, self.jobDict.keys())

    # TODO: add Bob multithread


if __name__ == "__main__":
    serverOnline = True
    jobPool = BobPool()
    jobPool.genJobDict()
    jobPool.getJobQueue()
    log = Logger()
    log.info(jobPool.jobQueue)
    jobPool.executeBob()
