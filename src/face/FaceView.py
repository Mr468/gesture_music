# coding:utf-8
# file: FaceView.py
# @author: CHEN
# @time: 2019/11/24 15:34
# @desc:
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QGridLayout, QLabel, QWidget
from cv2 import cv2


class FaceView(QWidget):
    def __init__(self):
        super(FaceView, self).__init__()
        self.label = QLabel(self)
        self.label.setFixedSize(400, 400)
        self.label.move(400, 350)
        # self.label.setText("显示录像")
        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;border-radius:100px;}"
                                 )
        # pix = QPixmap('res/rest.jpg')
        # self.label.setScaledContents(True)
        # self.label.setPixmap(pix)

        # 刷新摄像头的显示时间，实时显示
        self.timer = QTimer()
        self.timer.start()
        self.timer.setInterval(3)

        self.cap = cv2.VideoCapture(0)
        self.timer.timeout.connect(self.capPicture)

    """ 开启视频"""

    def capPicture(self):
        if (self.cap.isOpened()):
            # get a frame
            ret, img = self.cap.read()
            height, width, bytesPerComponent = img.shape
            bytesPerLine = bytesPerComponent * width
            # 变换彩色空间顺序
            cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
            # 转为QImage对象
            self.image = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(self.image).scaled(self.label.width(), self.label.height()))

    """ 停止录像"""

    def closeVideo(self):
        self.cap.release()
        self.label.setText(" ")
