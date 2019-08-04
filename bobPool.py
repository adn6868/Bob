from bob import Bob
import os
import pprint as pp
from logger.logger import Logger
log = Logger('bobPool')

def getJobList():
    jobList = {}
    for root, dirs, files in os.walk('schedule'):
        for file in files:
            with open(os.path.join(root, file), "r") as auto:
                fileData = {}
                for line in auto:
                    line = line.split(':')
                    fileData[line[0]] = line[1]
                jobList[auto.name] = fileData
    return jobList

if __name__ == "__main__":
    serverOnline = True
    jobList = getJobList()
    pp.pprint(jobList)
    log.infoB(jobList)
    
