from bob import Bob
import os
import pprint as pp
from logger.logger import Logger
import queue as Q
import datetime as dt
log = Logger('bobPool')


class PriorityQueue(object):
    def __init__(self):
        self.queue = []
    def enQueue(self, job):
        startTime = job.start


class BobPool(object):
    def __init__(self, name = 'Bob Pool: Chicago 01'):
        self.__name__ = name
        self.jobList = {}
        self.jobQueue = Q.PriorityQueue()
    def getJobList(self,osPath = 'schedule'): # TODO: TOkken handling this
        for root, dirs, files in os.walk(osPath):
            for file in files:
                with open(os.path.join(root, file), "r") as auto:
                    fileData = {}
                    for line in auto:
                        line = line.split(':')
                        fileData[line[0].strip(' ')] = ''.join(line[1:])
                    self.jobList[auto.name] = fileData
    def getJobQueue(self):
        for job in self.jobList:
            jobDetail = self.jobList[job]
            self.jobQueue.put((jobDetail['start'],job))

    # TODO: add priority Queue in Bob
    # TODO: add Bob multithread



if __name__ == "__main__":
    serverOnline = True
    jobPool = BobPool()
    jobPool.getJobList()
    jobPool.getJobQueue()
    pp.pprint(jobPool.jobList)
    while not jobPool.jobQueue.empty():
        pp.pprint(jobPool.jobQueue.get())
    
