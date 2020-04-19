import datetime


class BackLog:
    def __init__(self, project):
        self.project = project
        self.startTime = datetime.datetime.now()
        self.LOG = []
        self.size = 0
