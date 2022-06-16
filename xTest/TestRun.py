import pytest
import sys
import os
import time
import ast
from datetime import datetime
from common.ConfigUtil import BaseConfigUtil
from common.BaseCode import BaseCode
from common.AssertUtil import AssertUtil
from common.SSHUtil import SSHUtil
import common.Global as gol

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
configFilePath = os.path.abspath(
    os.path.join(rootPath, 'config', 'config.ini'))

# class TestRun:
#     def __init__(self):
#         config = ConfigUtil(configFilePath)
#         reportPath = config.config.get("platform", "report_path")
#         reportPath = os.path.abspath(
#             os.path.join(rootPath, reportPath + str(datetime.now().strftime("%Y%m%d%H%M%S")) + ".html"))
#         self.curPath = curPath
#         self.rootPath = rootPath

basecode = BaseCode()
assertUtil = AssertUtil()
baseConfig = BaseConfigUtil()
serverScriptPath = baseConfig.getServerScriptPaht()


@pytest.mark.parametrize('caseData', basecode.getCaseDataList("Sheet1"))  # 执行指定用例（从excel读取数据）
def testRun(caseData):
    caseId = caseData['caseId']
    caseTitle = caseData['caseTitle']
    server = caseData['server']
    port = 22
    serverUser = caseData['serverUser']
    serverPasswd = caseData['serverPasswd']
    scriptFilePath = caseData['script']
    expectRes = caseData['expectRes']

    """
    连接服务器执行用例：
        1、连接服务器
        2、在服务器指定目录(config.ini=>server_testscript_path)中建立以用例脚本所在目录的目录名命名的文件夹
        3、上传用例脚本所在目录中所有文件到服务器刚刚建立的文件夹中
        4、执行指定的用例脚本，接受返回结果
        5、删除上传的脚本及目录
        6、比较返回结果与预期结果
    """

    # 1 连接服务器
    sshutil = SSHUtil(server, port, serverUser, str(serverPasswd))
    sshutil.connect()

    # 2 在服务器指定目录(config.ini=>server_testscript_path)中建立以用例脚本所在目录的目录名命名的文件夹
    sshutil.exec("rm -rf " + serverScriptPath)
    time.sleep(5)
    sshutil.exec("mkdir -p " + serverScriptPath)

    # 3 上传用例脚本所在目录中所有文件到服务器刚刚建立的文件夹中
    # TODO 集成从SVN中取脚本文件并上传
    sshutil.upload(os.path.dirname(scriptFilePath), serverScriptPath)

    # 4 执行指定的用例脚本，接受返回结果
    workdir = serverScriptPath + os.sep + os.path.split(os.path.dirname(scriptFilePath))[1] + os.sep
    sshutil.exec("chmod 755 " + workdir + " *.sh")
    cmd ='cd ' + workdir+';sh ' + workdir + os.path.split(scriptFilePath)[1]
    sshrtn = sshutil.exec(cmd)

    # 5
    # sshutil.exec("rm -rf " + serverScriptPath)
    # time.sleep(5)

    rtn = sshrtn.read().decode('utf-8').strip()
    # print("rtn: " + rtn)
    # print("exp: " + expectRes)

    sshutil.close()
    assertUtil.assertEqual(caseId=caseId, caseName=caseTitle, res=rtn, expected=expectRes)
