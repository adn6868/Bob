import datetime
import sys
import pprint as pp
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
    def infoB(self, uglyData):
        rv = " {}: {}:\n {}\n".format(self.getTime(), self.name, beautyData)
        sys.stdout.write(beautyData)


def foo(name):ls
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name


if __name__ == '__main__':
    a = foo("anh")
    print(a.getName())

