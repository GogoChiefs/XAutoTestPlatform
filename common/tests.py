from django.test import TestCase
import sys
import os
import re
import operator
import ast

from common.ExcelUtil import ExcelUtil
from common.ConfigUtil import ConfigUtil
from common.BaseCode import BaseCode
from common.SSHUtil import SSHUtil
from common.LogUtil import LogUtil

from datetime import datetime, timedelta, timezone

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class ExcelUtilTests(TestCase):
    def setUp(self):
        """"""
        print(curPath)
        print(rootPath)
        print(os.path.split(curPath))

    def tearDown(self):
        """"""

    def testExcelUtil(self):
        excel_path = "/Users/zhangbolun/Documents/PythonProjects/xTestPlatform/temporary/testcase.xlsx"
        workbook = ExcelUtil(excel_path)
        print(workbook.get_sheetnames())
        print(workbook.get_colnum("Sheet1"))
        print(workbook.get_rownum("Sheet1"))
        print(workbook.get_content("Sheet1", 1, 4))
        print(workbook.release())


class ConfigUtilTests(TestCase):
    def setup(self):
        """"""

    def teardown(self):
        """"""

    def testConfigUtil(self):
        # print(os.path.dirname(__file__))
        # print(curPath)
        # print(rootPath)
        # print(os.path.split(curPath))
        # file = os.path.abspath(os.path.join(os.getcwd(), '..', 'config', file_name))
        # print(os.getcwd())
        # print(sys.path[1])
        # print(os.path.dirname(__file__))

        configFilePath = os.path.abspath(
            os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.ini'))
        # print(configFilePath)
        config = ConfigUtil(configFilePath)
        print('sections: ', config.config.sections())
        print('items: ', config.config.options('platform'))
        print('item: ', config.config.get('platform', 'testcase_path'))


class BaseCodeTest(TestCase):
    def testBaseCode(self):
        baseCode = BaseCode()
        # caseList = baseCode.getCaseDataList("Sheet1")
        # print(caseList)
        testcaseNamesStr = baseCode.getTestcaseNameList("Sheet1")
        print(testcaseNamesStr)

class SSHUtilTest(TestCase):
    def testSSHUtil(self):
        ip = "172.16.196.134"
        port = 22
        username = "root"
        password = "111111"

        sshutil = SSHUtil(ip, port, username, password)
        sshutil.connect()
        # rtn = sshutil.exec("date")
        # rtn = rtn.read().decode('utf-8')
        # print('return: ', rtn)

        # sshutil.upload("/Users/zhangbolun/Documents/PythonProjects/xTestPlatform/temporary/test.sh", "/opt/test.sh")
        sshutil.upload("/Users/zhangbolun/Documents/PythonProjects/xTestPlatform/temporary/testscript/case370", "/opt/testscript")

        sshutil.close()


class LogUtilTest(TestCase):
    def testLogUtil(self):
        logg1 = LogUtil()
        logg1.info("测试info")
        logg1.warning("测试warning")
        logg1.debug("测试debug")
        logg1.error("测试error")

        logg2 = LogUtil()
        logg2.info("测试info g")
        logg2.warning("测试warning g")
        logg2.debug("测试debug g")
        logg2.error("测试error g")


class TestA(TestCase):

    def test(self):
        str1 = '"TRUE"'
        str2 = '"true"'
        str3 = 'True'
        print(eval(str1))
        print(eval(str2))
        print(eval(str3))

        print(isinstance(eval(str1), bool))
        print(isinstance(eval(str2), bool))
        print(isinstance(eval(str3), bool))
        # print(curPath)
        # testscriptPath = os.path.abspath(os.path.join(rootPath, 'temporary', 'testscript', 'case370', 'test.sh'))
        # print(os.path.split(testscriptPath)[1])
        # dicte = "{'A':'a','B':'b'}"
        # liste = "['a','b','c','d']"
        # stre = "dfklafdksa"
        #
        # print(isinstance(eval(dicte), dict))
        # print(isinstance(eval(liste), list))
        #
        # print(isinstance(ast.literal_eval(dicte), dict))
        # print(isinstance(ast.literal_eval(liste), list))
        #
        # print()
        # print(testscriptPath)
        # print(os.path.dirname(testscriptPath))
        # print(os.walk(testscriptPath))
        # print(os.path.isfile(testscriptPath))
        # print(os.path.split(os.path.dirname(testscriptPath))[1])
        # print("opt" + os.sep + "test")
        # remotepath='/opt/testscript'
        # fatPath = os.path.split(os.path.dirname(testscriptPath))[0]
        # dirname = os.path.split(os.path.dirname(testscriptPath))[1]
        # print(fatPath)
        # print(dirname)
        # print(remotepath)

        # for root, dirs, files in os.walk(os.path.dirname(testscriptPath)):
        #     print(root)
        #     print(root.replace(fatPath, ""))
        #     workdir = remotepath + root.replace(fatPath, "")
        #     print("workdir:"+workdir)
        # for root, dirs, files in os.walk(testscriptPath):
        #     print(root)
        #     print(dirs)
        #     print(files)
        # print(os.listdir(testscriptPath))
        # a = '[{"code":"ceshi006","description":"测试006","parent":"ceshi003","parentDesc":"测试003","childs":[]},{"code":"zidonghuaceshi001","description":"自动化测试001","parent":"ceshi003","parentDesc":"测试003","childs":[]},{"code":"ceshi004","description":"测试006","parent":"ceshi003","parentDesc":"测试003","childs":[]},{"code":"zidonghu001","description":"自动化001","parent":"ceshi003","parentDesc":"测试003","childs":[]},{"code":"zidonghuaceshi005","description":"自动化测试005","parent":"ceshi003","parentDesc":"测试003","childs":[]},{"code":"zidonghuaceshi002","description":"测试003qweri！@#￥%qwertasdfghjkl;asdfg","parent":"ceshi003","parentDesc":"测试003","childs":[]}]'
        # b = '"[zidonghuaceshi005] is existed"'
        # c = 'basbsbssbabsbs'
        # print(eval(c))

        # expected = 'za\nfdkslaflkdsa\nfdsa\rldsa\tdfsajlkfdlsak'
        # print(expected)
        # res = re.sub("\s", "", expected)
        # print(res)

        # str1 = 'jkldfsofi129ihn923n2jfri3291n9i-fj120-21'
        # rexStr1 = re.search("jsjjj*", str1, re.I)
        # print(rexStr1.group())
        # print(rexStr1.groups())
        # print(rexStr1.groupdict())

        # print(isinstance("baba", list))
        # list1 = [{'name': 'zhangsan', 'age': '20'}, {'name': 'lisi', 'age': '21'}]
        # list2 = [{'name': 'lisi', 'age': '21'}, {'name': 'zhangsan', 'age': '20'}]
        # list3 = [{'name': 'zhangsan', 'age': '2321'}, {'name': 'lisi', 'age': '21'}]
        # list4 = [{'nam': 'zhangsan', 'age': '20'}, {'nam': 'lisi', 'age': '21'}]
        # list5 = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
        # list6 = [[2, 3, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
        # list7 = [[1, 1, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
        # list8 = [{'a': [{'a1': 'a1', 'a2': 'a2'}, {'a3': 'a3', 'a4': 'a4'}], 'b': ['b1', 'b2', 'b3', 'b4']}]
        # list9 = [{'b': ['b1', 'b2', 'b3', 'b4'], 'a': [{'a1': 'a1', 'a2': 'a2'}, {'a3': 'a3', 'a4': 'a4'}]}]
        # list10 = [{'a': [{'a1': 'a2', 'a1': 'a2'}, {'a3': 'a3', 'a4': 'a4'}], 'b': ['b1', 'b2', 'b3', 'b4']}]
        # print(operator.eq(list1, list2))
        # print(operator.eq(list1, list3))
        # print(operator.eq(list1, list4))
        # print(operator.eq(list5, list6))
        # print(operator.eq(list5, list7))
        # print(operator.eq(list8, list9))
        # print(operator.eq(list8, list10))
        #
        # dict1 = {'name': 'zhangsan', 'age': '1'}
        # dict2 = {'age': '1', 'name': 'zhangsan'}
        # dict3 = {'name': 'lisi', 'age': '1'}
        # dict4 = {'nam': 'zhangsan', 'age': '1'}
        # dict5 = {'list1': [1, 2, 3, 4], 'list2': [5, 6, 7, 8]}
        # dict6 = {'list2': [5, 6, 7, 8], 'list1': [1, 2, 3, 4]}
        # dict7 = {'list1': [1, 2, 3, 4], 'list2': [5, 6, 7, 8], 'list3': [9, 10, 11, 12]}
        # print(operator.eq(dict1, dict2))
        # print(operator.eq(dict1, dict3))
        # print(operator.eq(dict1, dict4))
        # print(operator.eq(dict5, dict6))
        # print(operator.eq(dict5, dict7))
        # print(operator.contains(dict7, dict5))

        # print(str(datetime.now().strftime("%Y%m%d%H%M%S")))
        # print(datetime.utcnow().astimezone(timezone(timedelta(hours=8),name='Asia/Shanghai')).strftime("%Y%m%d%H%M%S"))

        # dict1 = {'a': 'a1', 'b': 'b1'}
        # ks, vs = dict1.items()
        # print(ks)
        # print("==========")
        # print(vs)
        # list1 = [0, 1, 2, 3]
        # list2 = ['a', dict1, list1]
        # list3 = ['b', 'c']
        # list4 = ['3', 2313]
        # list5 = list3 + list2 + list4
        # print(list5)
        # print(list5.index(eval("{'a': 'a', 'b': 'c'}")))

        # self.assertIncludeList(list5, eval("[{'a': 'a', 'b': 'c'}]"))
        # print(list2.index('a'))
        # print(list2.index(eval("{'a': 'a', 'b': 'b'}")))
        # print(list2[1])
        # print(list2.index(list2[1]))
        # print(list2.index(eval("[0, 1, 2, 3]")))
        #
        # set1 = set(eval("{'a':'a','b':'b'}"))
        # set2 = set(eval("{'a':'a','b':'b', 'c':'c'}"))
        # print(set1.issubset(set2))
        # print(set2.issubset(set1))
