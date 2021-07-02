import json
import urllib

import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(332, 120)
        MainWindow.setMinimumSize(QtCore.QSize(332, 120))
        MainWindow.setMaximumSize(QtCore.QSize(332, 120))
        MainWindow.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 90, 331, 28))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background-color: rgb(20, 255, 255);\n"
                                      "background-color: rgb(10, 221, 179);\n"
                                      "border-style: outset;\n"
                                      "border-width: 1px;\n"
                                      "border-radius: 10px;\n"
                                      "border-color: rgb(50, 50, 50);\n"
                                      "font: bold 14px;\n"
                                      "min-width: 10em;\n"
                                      "padding: 6px;}\n"
                                      "QPushButton::hover\n"
                                      "{\n"
                                      "background-color: rgb(10, 201, 109);\n"
                                      "}\n"
                                      "QPushButton::pressed\n"
                                      "{\n"
                                      "background-color: rgb(10, 121, 79);\n"
                                      "}\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onclick)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 50, 50))
        self.label.setMinimumSize(QtCore.QSize(50, 50))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 271, 50))
        self.label_2.setMinimumSize(QtCore.QSize(0, 50))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 331, 31))
        self.lineEdit.setStyleSheet("border-style: outset;\n"
                                    "border-width: 1px;\n"
                                    "border-radius: 10px;    \n"
                                    "border-color: rgb(50, 50, 50);\n"
                                    "background-color: rgb(109, 109, 109);\n"
                                    "padding: 6px;\n"
                                    "color: rgb(176, 176, 176);\n"
                                    "")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pyweather"))
        self.pushButton.setText(_translate("MainWindow", "Get weather"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "City"))

    def onclick(self):
        city = self.lineEdit.text()
        if city != "":
            try:
                url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID=18ad553a7ecce109726c14735c96fc44"
                response = requests.get(url)
                data = json.loads(response.text)
                self.label_2.setText(f"{data['weather'][0]['description']} {data['main']['temp']} C")
                pdata = urllib.request.urlopen(
                    f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png").read()
                qim = QImage()
                qim.loadFromData(pdata)
                pixmap = QPixmap.fromImage(qim)
                self.label.setPixmap(pixmap)
            except:
                pass
