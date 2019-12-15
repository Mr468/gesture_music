# coding:utf-8
# file: FileUtil.py
# @author: Hou
# @contact: houz_work@163.com
# @time: 2019/11/24 14:19
# @desc:文件相关的工具类
import base64
import os


class FileUtil(object):

    @staticmethod
    def get_dir_path(project_name, relative_path):
        """
        获取指定文件夹路径
        :param project_name:项目名称
        :param relative_path:相对路径
        :return:
        """
        cur_path = os.path.abspath(os.path.dirname(__file__))
        root_path = cur_path[:cur_path.find(project_name + '\\') + len(project_name + '\\')]
        path = root_path + relative_path
        return path

    @staticmethod
    def get_file_content(file_path):
        """
        获取文件流
        :param file_path: 文件路径
        :return:流文件
        """
        with open(file_path, 'rb') as fp:
            return fp.read()

    @staticmethod
    def get_file_content_base64(file_path):
        """
        获取64位编码后的文件
        :param file_path: 文件路径
        :return: 64位编码后的文件
        """
        return base64.b64encode(FileUtil.get_file_content(file_path))
