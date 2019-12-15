# coding:utf-8
# file: SpeechView.py
# @author: Hou
# @contact: houz_work@163.com
# @time: 2019/11/24 15:16
# @desc:语音界面
from PyQt5.QtWidgets import QDialog

from layout.ui_speech import Ui_MainWindow
from src.FaceView import FaceView
from src.base.BaseWindow import BaseWindow


class SpeechView(Ui_MainWindow, BaseWindow):

    def __init__(self, main_window):
        super().__init__(main_window)
        self.setupUi(main_window)
        self.init_view()
        self.init_click()

    def init_view(self):
        pass

    def init_click(self):
        self.pushButton.clicked.connect(self.start_new_ui)

    def start_new_ui(self):
        print('跳转到新界面')
        form = QDialog()
        FaceView(form)
        form.show()
        form.exec_()
