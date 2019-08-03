import datetime
import sys
class Logger(object):
    def __init__ (self, name =__name__):
        self.name = name
    def getTime(self, tz = None):
        return str(datetime.datetime.now(tz = tz))
        
    def info(self, data):
        try:
            data = str(data)
        except:
            raise IOError
        rv = " {}: {}: {}\n".format(self.getTime(), self.name, data)
        sys.stdout.write(rv)