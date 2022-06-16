import logging
import sys
import os
import xlrd


class ExcelUtil:
    """
    Excel文件处理工具类
    """

    """
    构造函数
    初始化Excel文件对象
    """

    def __init__(self, excelPath):
        self.excelPath = excelPath
        try:
            self.workbook = xlrd.open_workbook(excelPath, on_demand=True)
        except BaseException as e:
            # TODO 增加日志机制
            logging.ERROR(e)

    """
    获取sheet对象
    :param sheet_name: 表单名
    :return:
    """

    def get_sheet(self, sheetName):
        try:
            sheet = self.workbook.sheet_by_name(sheetName)
            return sheet
        except BaseException as e:
            logging.ERROR("打开 Sheet失败失败：%s" % e)

    """
    获取sheet_name
    """

    def get_sheetnames(self):
        try:
            sheet_names = self.workbook.sheet_names()
            return sheet_names
        except BaseException as e:
            logging.ERROR("获取sheet名失败: %s" % e)

    """
    获取sheet行数
    """
    def get_rowcount(self, sheetName):
        try:
            sheet = self.get_sheet(sheetName)
            rowcount = sheet.nrows
            return rowcount
        except BaseException as e:
            logging.ERROR("获取sheet行数失败: %s" % str(e))

    """
    获取sheet列数
    """
    def get_colcount(self, sheetName):
        try:
            sheet = self.get_sheet(sheetName)
            colcount = sheet.ncols
            return colcount
        except BaseException as e:
            logging.ERROR("获取sheet列数失败: %s" % str(e))

    """
    获取表格内容
    :param row:行
    :param col:列
    :return:String
    """
    def get_content(self, sheetName, row, col):
        sheet = self.get_sheet(sheetName)
        cell_value = sheet.cell_value(int(row), int(col))
        if type(cell_value) == float:
            return int(cell_value)
        return cell_value

    """
    释放excel对象
    """
    def release(self):
        self.workbook.release_resources()