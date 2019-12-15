# coding:utf-8
# file: BaseWindow.py
# @author: Hou
# @contact: houz_work@163.com
# @time: 2019/11/24 14:17
# @desc:窗口基类,提供一些公用的方法。
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from src.utils.FileUtil import FileUtil


class BaseWindow(object):

    def __init__(self, main_window):
        self.mainWindow = main_window

    def check_format(self, str_content):
        """
        检查输入的字符串格式是否正确，格式正确返回True，错误返回False
        :param str_content: 待检查的字符串
        :return:
        """
        if str_content == '':
            self.show_message_box('错误', '请检查输入内容')
            return False
        return True

    def show_message_box(self, title, content):
        """
        弹出一个消息框
        :param title: 消息标题
        :param content: 消息内容
        """
        QMessageBox.about(self.mainWindow, title, content)

    def show_file_select(self, project_name, dir_name, filter_style):
        """
        在当前项目下指定文件夹，打开文件选择界面
        :param project_name:项目名
        :param dir_name:指定文件夹名
        :param filter_style: 文件过滤格式
        :return:选中文件的路径
        """
        path = FileUtil.get_dir_path(project_name, dir_name)
        openfile_name = QFileDialog.getOpenFileName(self.mainWindow, '选择文件', path, filter_style)
        return openfile_name[0]
