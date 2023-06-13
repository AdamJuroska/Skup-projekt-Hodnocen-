import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSlot



class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'hodnocení'
        self.left = 20
        self.top = 20
        self.width = 850
        self.height = 500
        self.initUI()
        self.a=0
        self.b=0
        self.c=0
        self.d=0
        self.g =":)"
        self.q =":]"
        self.f =":/"
        self.r =":("
        self.setStyleSheet("background-color : lightblue")

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton(':)', self)
        button.setToolTip('nejspokojenější')
        button.move(150, 220)
        button.setStyleSheet("background-color : green")
        button.clicked.connect(self.on_click1)

        button1 = QPushButton(':]', self)
        button1.setToolTip('spokojený')
        button1.move(300, 220)
        button1.setStyleSheet("background-color : lightgreen")
        button1.clicked.connect(self.on_click2)

        button2 = QPushButton(':/', self)
        button2.setToolTip('nespokojený')
        button2.move(450, 220)
        button2.setStyleSheet("background-color : pink")
        button2.clicked.connect(self.on_click3)
