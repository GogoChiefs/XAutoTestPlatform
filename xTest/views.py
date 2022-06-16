from django.shortcuts import render
from datetime import datetime
from common.ExcelUtil import ExcelUtil
from common.LogUtil import LogUtil
from common.ConfigUtil import ConfigUtil
import os
import sys
import time
import chardet
import common.Global as glo
from subprocess import Popen, PIPE

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]

configFilePath = os.path.abspath(
    os.path.join(rootPath, 'config', 'config.ini'))
config = ConfigUtil(configFilePath)

testRunPath = os.path.abspath(os.path.join(rootPath, 'xTest', 'TestRun.py'))

log = LogUtil()
glo.set_value("log", log)


# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'templates/xTest/runTest.html', context={'testcase_file_name': ''})
    elif request.method == 'POST':
        testcaseFileName = request.POST.get("testcase_file_name")
        if testcaseFileName is None:
            sheetNum = ''

        reportPath = config.config.get("platform", "report_path")
        reportPath = os.path.abspath(
            os.path.join(rootPath, reportPath))

        cmd = "pytest -s {0} --html={1} --self-contained-html".format(testRunPath, reportPath + ".html")
        # cmd = "pytest -s {0} --alluredir={1}".format(testRunPath, reportPath)
        # log.info(cmd)
        glo.get_value("log").info(cmd)

        process = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        if stdout is not None:
            glo.get_value("log").info("stdout is not None")
            glo.get_value("log").info("stdoutType: " + str(type(stdout)))
            glo.get_value("log").info("stdoutCode: " + str(chardet.detect(stdout)))
            typeDict = chardet.detect(stdout)
            typeStr = typeDict.get("encoding")
            if typeStr is None or typeStr == "" or typeStr == "None":
                glo.get_value("log").info("stdout: " + stdout.decode("utf-8"))
            else:
                glo.get_value("log").info("stdout: " + stdout.decode(typeStr))
        if stderr is not None:
            glo.get_value("log").info("stderr is not None")
            glo.get_value("log").info("stderrType: " + str(type(stderr)))
            glo.get_value("log").info("stderrCode: " + str(chardet.detect(stderr)))
            # glo.get_value("log").info("stderr: " + stderr.decode("GB2312"))
            typeDict = chardet.detect(stderr)
            typeStr = typeDict.get("encoding")
            if typeStr is None or typeStr == "" or typeStr == "None":
                glo.get_value("log").info("stderr: " + stderr.decode("utf-8"))
            else:
                glo.get_value("log").info("stderr: " + stderr.decode(typeStr))

        return render(request, 'templates/xTest/runTest.html', context={'testcase_file_name': testcaseFileName})
