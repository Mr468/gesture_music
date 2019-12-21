# coding:utf-8
# file: MainWindow.py
# @author: Hou
# @contact: houz_work@163.com
# @time: 2019/12/21 11:40
# @desc:主界面
from qtpy import QtWidgets

from layout.ui_main import Ui_MainWindow
from src.speech.SpeechView import SpeechView


class MainWindow(Ui_MainWindow):
    def __init__(self, main_window):
        self.setupUi(main_window)
        child_window = QtWidgets.QMainWindow()
        speech_view = SpeechView(child_window, self)
        self.gridLayout.addWidget(speech_view.mainWindow)

    def start_child_window(self, old, new):
        old.hide()
        self.gridLayout.addWidget(new)
