# coding:utf-8
# file: Main.py.py
# @author: Hou
# @contact: houz_work@163.com
# @time: 2019/11/24 13:57
# @desc:程序入口文件
import os
import sys
import cgitb

from src.base.MainWindow import MainWindow

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

from PyQt5 import QtWidgets

cgitb.enable(format='text')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    mainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = MainWindow(mainWindow)  # ui是UiForm()类的实例化
    mainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication
