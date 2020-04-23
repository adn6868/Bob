import sys
from datetime import datetime as dt
print("Hello world!")
print("Hi it's {}\n I would like to say hi to the following people \n {}".format(dt.now(),sys.argv[1:]))