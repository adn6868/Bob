import datetime
from StatusConfig import STATUS_CONFIG


class BobTicket:
    def __init__(self, id, name="untitled"):
        self.name = name
        self.project = "TIK"
        self.id = id
        self.createTime = datetime.datetime.now()
        self.status = "Created"
        self.statusConfig = STATUS_CONFIG
        self.description = None
        self.tag = None
        self.attachment = None
        self.owner = "ANH"
        self.LOG = "{}| BoB Ticket Created  ".format(datetime.datetime.now())

    def getLog(self):
        return self.LOG

    def getDescription(self):
        return self.description

    def addDescription(self, description):
        self.description = description
        self.LOG += "{}| Detail updated to \n {} \n".format(
            datetime.datetime.now(), description
        )

    def assign(newWorker):
        self.owner = newWorker
        self.LOG += "{}| Ticket Assigned to {}\n".format(
            datetime.datetime.now(), newWorker
        )

    def changedStatus(status, newWorker=None):
        if status not in self.statusConfig.values():
            raise "TICKET STATUS NOT MATCH WITH CONFIG"
        self.status = status
        self.owner = newWorker if newWorker else self.owner
        self.LOG += "{}| Ticket Status updated: {} worker: {}\n".format(
            datetime.datetime.now(), self.status, self.owner
        )
