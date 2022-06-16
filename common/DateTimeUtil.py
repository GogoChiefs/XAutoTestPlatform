import os
import sys
from datetime import date, datetime, timezone, timedelta
import time

curPath = os.path.abspath(os.path.dirname(__name__))
rootPath = os.path.abspath(os.path.dirname(curPath))


class DateTimeUtil:
    def __init__(self):
        self.date = date
        self.time = time
        self.datetime = datetime().astimezone(tz=timezone(timedelta(hours=8)))

    def a(self):
        print(self.datetime.now())
        print(self.time.time())


if __name__ == '__main__':
    print(datetime.now())
    print(datetime.utcnow())
    print(datetime.now().strftime("%Y%m%d %H%M%S"))
