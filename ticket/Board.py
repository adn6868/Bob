import datetime


class Board:
    def __init__(self, project, id=0):
        self.project = project
        self.id = id
        self.startTime = datetime.datetime.now()
        self.endTime = self.startTime + datetime.timedelta(days=14)
        self.TODO = []
        self.WORKING = []
        self.TESTING = []
        self.DONE = []
