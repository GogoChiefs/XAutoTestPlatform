import os
import sys
import configparser
import logging

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.abspath(os.path.dirname(curPath))

"""
config.ini文件处理工具类
"""


class ConfigUtil:

    def __init__(self, configFilePath):
        try:
            # file = os.path.abspath(os.path.join(os.getcwd(), '..', 'config', file_name))
            self.configFilePath = configFilePath
            self.config = configparser.ConfigParser()
            self.config.read(self.configFilePath, encoding="utf-8")
        except BaseException as e:
            logging.ERROR("读取配置文件config.ini失败: %s" % str(e))


class BaseConfigUtil:
    def __init__(self):
        try:
            baseConfigPath = os.path.join(rootPath, 'config', 'config.ini')
            self.baseConfigPath = baseConfigPath
            self.config = configparser.ConfigParser()
            self.config.read(self.baseConfigPath, encoding='utf-8')
        except:
            print(1)

    def getTestcasePath(self):
        path = self.config.get('platform', 'testcase_path')
        return path

    def getReportPath(self):
        path = self.config.get('platform', 'report_path')
        return path

    def getLogPath(self):
        path = self.config.get('platform', 'log_path')
        return path

    def getServerScriptPaht(self):
        path = self.config.get('platform', 'server_testscript_path')
        return path