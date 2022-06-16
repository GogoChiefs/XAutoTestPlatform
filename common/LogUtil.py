import os
import sys
from datetime import datetime,timedelta,timezone
from loguru import logger
from common.ConfigUtil import BaseConfigUtil

curpath = os.path.abspath(os.path.dirname(__file__))
rootpath = os.path.abspath(os.path.dirname(curpath))

class LogUtil:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(LogUtil, cls).__new__(cls, *args, **kwargs)
            logpath = os.path.abspath(os.path.join(rootpath, BaseConfigUtil().getLogPath()))
            logger.add(
                f"{logpath}/xlog_{datetime.now(tz=timezone(timedelta(hours=8))).strftime('%Y_%m_%d_%H_%M_%S')}.log",
                rotation="500MB",
                encoding="utf-8",
                enqueue=True,
                retention="7 days",
                format="{time: YYYY-MM-DD HH:mm:ss.SSS Z+08:00 !UTC} | {level} | {message}")
        return cls.__instance

    def info(self, msg):
        return logger.info(msg)

    def debug(self, msg):
        return logger.debug(msg)

    def warning(self, msg):
        return logger.warning(msg)

    def error(self, msg):
        return logger.error(msg)