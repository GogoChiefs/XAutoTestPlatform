import os
import sys
import re
import operator
from common.LogUtil import LogUtil

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.abspath(os.path.dirname(curPath))
log = LogUtil()

"""
结果对比工具
要求excel中所有的expected结果都要用双引号括起来
"""


class AssertUtil:
    """
        判断字符串相等的断言方法
        :param expected : expected in excel
        :param res : response
    """

    def assertEqStr(self, expected, res):
        try:
            expected = re.sub("\s", "", expected)
            res = re.sub("\s", "", res)
            assert operator.eq(expected, res)
        except AssertionError:
            raise

    """
        判断List相等的断言方法
        :param expected
        :param res
    """

    def assertEqList(self, expected, res):
        try:
            # 因为operator模块可以对list进行相等判断，无论list中是字符串、dict、list，因此直接判断即可
            assert operator.eq(expected, res)
        except AssertionError:
            raise

    """
        判断Dict相等的断言方法
        :param expected
        :param res
    """

    def assertEqDict(self, expected, res):
        try:
            # 因为operator模块可以对dict进行相等判断，无论dict中是字符串、dict、list，因此直接判断即可
            assert operator.eq(expected, res)
        except AssertionError:
            raise

    """
        判断Str包含的断言方法
        expected pattern in string
        :param string
        :param pattern
    """

    def assertIncludeStr(self, string, pattern):
        try:
            string = re.sub("\s", "", string).lower()
            pattern = re.sub("\s", "", pattern).lower()
            assert pattern in string
        except AssertionError:
            raise

    """
        判断List包含的断言方法
        expected res in expected
        :param expected
        :param res
    """

    def assertIncludeList(self, expected, res):
        try:
            for item in res:
                assert expected.index(item)
        except ValueError:
            raise
        except AssertionError:
            raise

    """
        判断Dict包含的断言方法
        expected res in expected
        :param expected
        :param res
    """

    def assertIncludeDict(self, expected, res):
        try:
            exptectedSet = set(expected.items())
            resSet = set(res.items())
            assert resSet.issubset(exptectedSet)
        except AssertionError:
            raise

    """
    相等断言
    :param
    caseId: id of case, equals to chandao
    caseName: name of case, equals to chandao
    res: response of testcase
    expected: expected response of testcase
    """

    def assertEqual(self, caseId, caseName, res, expected):

        """处理excel中expected数据未用双引号括起来的情况"""
        try:
            expecteddata = eval(expected)
            resdata = eval(res)
            log.info("测试用例编号: {0} , 返回结果: {1} , 预期结果: {2} ".format(caseId, resdata, expecteddata))
        except:
            log.info("测试用例编号: {0} , 返回结果: {1} , 预期结果: {2} ".format(caseId, resdata, expected))
            try:
                self.assertEqStr(expected, resdata)
                log.info("测试用例编号: {0} , 测试结果: PASS".format(caseId))
            except AssertionError:
                log.info("测试用例编号: {0} , 测试结果: FAILED , 失败原因: (预期) {1} 和 (结果) {2} 不匹配 ".format(caseId, expected, res))
                raise
            return None

        # """若expected为字符串"""
        if isinstance(expecteddata, str):
            try:
                self.assertEqStr(expecteddata, resdata)
                log.info("测试用例编号: {0} , 测试结果: PASS".format(caseId))
            except AssertionError:
                log.info("测试用例编号: {0} , 测试结果: FAILED , 失败原因: (预期) {1} 和 (结果) {2} 不匹配 ".format(caseId, expected, res))
                raise
        # """若expected为列表"""
        elif isinstance(expecteddata, list):
            try:
                self.assertEqList(expecteddata, resdata)
                log.info("测试用例编号: {0} , 测试结果: PASS".format(caseId))
            except AssertionError:
                log.info("测试用例编号: {0} , 测试结果: FAILED , 失败原因: (预期) {1} 和 (结果) {2} 不匹配 ".format(caseId, expected, res))
                raise
        # 若expected为字典
        elif isinstance(expecteddata, dict):
            try:
                self.assertEqDict(expecteddata, resdata)
                log.info("测试用例编号: {0} , 测试结果: PASS".format(caseId))
            except AssertionError:
                log.info("测试用例编号: {0} , 测试结果: FAILED , 失败原因: (预期) {1} 和 (结果) {2} 不匹配 ".format(caseId, expected, res))
                raise

    """
        包含断言
        :param
        caseId: id of case, equals to chandao
        caseName: name of case, equals to chandao
        res: response of testcase
        expected: expected response of testcase
    """

    def assertInclude(self, caseId, caseName, res, expected):
        """处理excel中expected数据未用双引号括起来的情况"""
        try:
            expecteddata = eval(expected)
            log.info("测试用例编号: {0} , 返回结果: {1} , 预期结果: {2} ".format(caseId, res, expecteddata))
        except:
            log.info("测试用例编号: {0} , 返回结果: {1} , 预期结果: {2} ".format(caseId, res, expected))
            rexRes = re.search(expected, res, re.I)
            if rexRes is None:
                # isNone代表expected中写的不是正则表达式或根据正则未搜索到 , 当成字符串处理
                try:
                    self.assertIncludeStr(expected, res)
                    log.info("测试用例编号: {0} , 测试结果: PASS".format(caseId))
                except AssertionError:
                    log.info(
                        "测试用例编号: {0} , 测试结果: FAILED , 失败原因: (预期) {1} 和 (结果) {2} 不为包含关系 ".format(caseId, expected, res))
                    raise
            else:
                try:
                    # assert rexExpected.group() in res
                    self.assertIncludeStr(expected, rexRes.group())
                    log.info("测试用例编号: {0} , 测试结果: PASS".format(caseId))
                except AssertionError:
                    log.info(
                        "测试用例编号: {0} , 测试结果: FAILED , 失败原因: (预期) {1} 和 (结果) {2} 不为包含关系 ".format(caseId, expected, res))
                    raise
        # 字符串
        if (isinstance(expecteddata, str)):
            try:
                self.assertIncludeStr(expecteddata, res)
                log.info("测试用例编号: {0} , 测试结果: PASS".format(caseId))
            except AssertionError:
                log.info(
                    "测试用例编号: {0} , 测试结果: FAILED , 失败原因: (预期) {1} 和 (结果) {2} 不为包含关系 ".format(caseId, expecteddata, res))
                raise
        # 字典
        elif (isinstance(expecteddata, dict)):
            try:
                self.assertIncludeDict(expecteddata, res)
                log.info("测试用例编号: {0} , 测试结果: PASS".format(caseId))
            except AssertionError:
                log.info(
                    "测试用例编号: {0} , 测试结果: FAILED , 失败原因: (预期) {1} 和 (结果) {2} 不为包含关系 ".format(caseId, expecteddata, res))
                raise
        # 列表
        elif (isinstance(expecteddata, list)):
            try:
                self.assertIncludeList(expecteddata, res)
                log.info("测试用例编号: {0} , 测试结果: PASS".format(caseId))
            except AssertionError:
                log.info(
                    "测试用例编号: {0} , 测试结果: FAILED , 失败原因: (预期) {1} 和 (结果) {2} 不为包含关系 ".format(caseId, expecteddata, res))
                raise
            except ValueError:
                log.info(
                    "测试用例编号: {0} , 测试结果: FAILED , 失败原因: (预期) {1} 和 (结果) {2} 不为包含关系 ".format(caseId, expecteddata, res))
                raise
        # 无法判定类型，按大字符串处理
        else:
            try:
                self.assertIncludeStr(expecteddata, res)
                log.info("测试用例编号: {0} , 测试结果: PASS".format(caseId))
            except AssertionError:
                log.info(
                    "测试用例编号: {0} , 测试结果: FAILED , 失败原因: (预期) {1} 和 (结果) {2} 不为包含关系 ".format(caseId, expecteddata, res))
                raise
