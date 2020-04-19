import datetime
import sys
import pprint as pp


class Logger(object):
    def __init__(self, name=__file__):
        self.name = name

    def getTime(self, tz=None):
        return str(datetime.datetime.now(tz=tz))

    def info(self, data):
        try:
            data = str(data)
        except:
            raise IOError
        rv = " {}: {}: {}\n".format(self.getTime(), self.name, data)
        sys.stdout.write(rv)

    def infoB(self, uglyData):
        rv = " {}: {}:\n {}\n".format(self.getTime(), self.name, uglyData)
        sys.stdout.write(uglyData)


if __name__ == "__main__":
    log = Logger()
    log.info("Hi world")
