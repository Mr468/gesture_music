# coding:utf-8
# file: SpeechView.py
# @author: Hou
# @contact: houz_work@163.com
# @time: 2019/11/24 15:16
# @desc:语音界面
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog

from layout.ui_speech import Ui_MainWindow
from src.FaceView import FaceView
from src.base.BaseWindow import BaseWindow
from aip import AipSpeech
from src.speech.Record import Record
from src.utils.FileUtil import FileUtil


class SpeechView(Ui_MainWindow, BaseWindow):
    App_id = '17339795'
    Api_key = 'VUluy7HdSdLETs3tRyAu4fzf'
    Secret_key = 'oeodkVzGnQGSz6VLev1WqvOajCuAbFnu'

    def __init__(self, main_window):
        super().__init__(main_window)
        self.setupUi(main_window)
        self.mainWindow = main_window
        self.init_view()
        self.if_record = True
        self.record = Record(self)
        self.record_path = 'tmp/record.wav'
        self.thread = SpeechThread(self)
        self.thread.start()
        self.thread.trigger.connect(self.on_work_finished)

    def init_view(self):
        """
        初始化界面
        """
        pix = QPixmap('res/rest.jpg')
        self.label.setScaledContents(True)
        self.label.setPixmap(pix)

    def start_work(self):
        """
        开始执行语音唤醒任务
        :return:语音识别结果
        """
        self.record.get_audio(self.record_path)
        return self.asr()

    def asr(self):
        """
        请求百度AI接口，进行语音识别
        :return:识别结果
        """
        client = AipSpeech(SpeechView.App_id, SpeechView.Api_key, SpeechView.Secret_key)
        result = client.asr(FileUtil.get_file_content(self.record_path), 'wav', 16000, )
        print(result)
        return result

    def on_work_finished(self, result):
        """
        线程执行完毕后的回调函数
        :param result:
        """
        if result['err_msg'] == 'success.' and result['result'][0].find('你好') != -1:
            self.start_new_ui()
        else:
            self.thread = SpeechThread(self)
            self.thread.start()
            self.thread.trigger.connect(self.on_work_finished)

    def start_new_ui(self):
        """
        开启新界面
        """
        self.mainWindow.close()
        form = QDialog()
        FaceView(form)
        form.show()
        form.exec_()


class SpeechThread(QThread):
    """
    语音线程类
    """
    trigger = pyqtSignal(dict)

    def __init__(self, speech_view):
        super(SpeechThread, self).__init__()
        self.speech_view = speech_view

    def run(self) -> None:
        result = self.speech_view.start_work()
        self.trigger.emit(result)