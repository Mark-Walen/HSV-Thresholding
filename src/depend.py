# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'depend.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(720, 670)
        mainWindow.setMinimumSize(QtCore.QSize(720, 670))
        mainWindow.setMaximumSize(QtCore.QSize(720, 670))
        mainWindow.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.div_line = QtWidgets.QFrame(self.centralwidget)
        self.div_line.setGeometry(QtCore.QRect(120, 510, 471, 20))
        self.div_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.div_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.div_line.setObjectName("div_line")
        self.hue_horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.hue_horizontalSlider.setGeometry(QtCore.QRect(179, 540, 350, 20))
        self.hue_horizontalSlider.setStyleSheet("")
        self.hue_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.hue_horizontalSlider.setMaximum(255)
        self.hue_horizontalSlider.setObjectName("hue_horizontalSlider")
        self.saturation_horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.saturation_horizontalSlider.setGeometry(QtCore.QRect(180, 580, 350, 16))
        self.saturation_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.saturation_horizontalSlider.setMaximum(255)
        self.saturation_horizontalSlider.setObjectName("saturation_horizontalSlider")
        self.value_horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.value_horizontalSlider.setGeometry(QtCore.QRect(180, 620, 350, 16))
        self.value_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.value_horizontalSlider.setMaximum(255)
        self.value_horizontalSlider.setObjectName("value_horizontalSlider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 640, 480))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../assets/cv.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.hue_label = QtWidgets.QLabel(self.centralwidget)
        self.hue_label.setGeometry(QtCore.QRect(70, 540, 28, 17))
        self.hue_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.hue_label.setObjectName("hue_label")
        self.saturation_label = QtWidgets.QLabel(self.centralwidget)
        self.saturation_label.setGeometry(QtCore.QRect(70, 580, 72, 17))
        self.saturation_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.saturation_label.setObjectName("saturation_label")
        self.value_label = QtWidgets.QLabel(self.centralwidget)
        self.value_label.setGeometry(QtCore.QRect(70, 620, 39, 17))
        self.value_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.value_label.setObjectName("value_label")
        self.hue_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.hue_lineEdit.setGeometry(QtCore.QRect(570, 540, 81, 21))
        self.hue_lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.hue_lineEdit.setReadOnly(True)
        self.hue_lineEdit.setObjectName("hue_lineEdit")
        self.saturation_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.saturation_lineEdit.setGeometry(QtCore.QRect(570, 580, 81, 21))
        self.saturation_lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.saturation_lineEdit.setReadOnly(True)
        self.saturation_lineEdit.setObjectName("saturation_lineEdit")
        self.value_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.value_lineEdit.setGeometry(QtCore.QRect(570, 620, 81, 21))
        self.value_lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.value_lineEdit.setReadOnly(True)
        self.value_lineEdit.setObjectName("value_lineEdit")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.hue_label.setText(_translate("mainWindow", "Hue"))
        self.saturation_label.setText(_translate("mainWindow", "Saturation"))
        self.value_label.setText(_translate("mainWindow", "Value"))
        self.hue_lineEdit.setText(_translate("mainWindow", "0"))
        self.saturation_lineEdit.setText(_translate("mainWindow", "0"))
        self.value_lineEdit.setText(_translate("mainWindow", "0"))
