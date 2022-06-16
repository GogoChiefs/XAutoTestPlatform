import sys
import os
from common.ExcelUtil import ExcelUtil
from common.ConfigUtil import ConfigUtil

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]


class BaseCode:
    def __init__(self):
        self.curPath = curPath
        self.rootPath = rootPath

    """
    按行获取testcase excel文件中用例数据
    """

    def getCaseDataList(self, sheetName):
        caseList = []
        configFilePath = os.path.abspath(
            os.path.join(self.rootPath, 'config', 'config.ini'))
        config = ConfigUtil(configFilePath)
        testcaseFilePath = os.path.abspath(
            os.path.join(self.rootPath, config.config.get('platform', 'testcase_path'))
        )
        workbook = ExcelUtil(testcaseFilePath)
        rowCount = workbook.get_rowcount(sheetName)
        for rowNum in range(1, rowCount):
            caseId = workbook.get_content(sheetName, rowNum, config.config.get("testcase_excel", "case_id"))
            caseTitle = workbook.get_content(sheetName, rowNum, config.config.get("testcase_excel", "case_title"))
            caseType = workbook.get_content(sheetName, rowNum, config.config.get("testcase_excel", "case_type"))
            server = workbook.get_content(sheetName, rowNum, config.config.get("testcase_excel", "server"))
            serverUser = workbook.get_content(sheetName, rowNum, config.config.get("testcase_excel", "server_user"))
            serverPasswd = workbook.get_content(sheetName, rowNum, config.config.get("testcase_excel", "server_passwd"))
            container = workbook.get_content(sheetName, rowNum, config.config.get("testcase_excel", "container"))
            script = workbook.get_content(sheetName, rowNum, config.config.get("testcase_excel", "script"))
            expectRes = str(workbook.get_content(sheetName, rowNum, config.config.get("testcase_excel", "expectRes")))
            assertType = workbook.get_content(sheetName, rowNum, config.config.get("testcase_excel", "assert_type"))
            errorOccur = workbook.get_content(sheetName, rowNum, config.config.get("testcase_excel", "error_occur"))
            errorOccurSkip = workbook.get_content(sheetName, rowNum,
                                                  config.config.get("testcase_excel", "error_occur_skip"))
            caseDict = {"caseId": caseId, "caseTitle": caseTitle, "caseType": caseType, "server": server,
                        "serverUser": serverUser, "serverPasswd": serverPasswd,
                        "container": container, "script": script, "expectRes": expectRes, "assertType": assertType,
                        "errorOccur": errorOccur, "errorOccurSkip": errorOccurSkip}
            caseList.append(caseDict)

        return caseList