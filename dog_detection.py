# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dogdetection.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog,QDialog,QLabel
from PyQt5.QtGui import QPixmap
import sys
import cv2
import test_image
import detect_rc

###############################################################################
###############################################################################


class Ui_MainWindow(QtWidgets.QWidget):
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1024)
        palette = QtGui.QPalette()
        myPixmap = QtGui.QPixmap('E:\\project\\minor project 2\\ppt\\ccc.jpg')
        myScaledPixmap = myPixmap.scaled(self.size(), QtCore.Qt.KeepAspectRatio, transformMode = QtCore.Qt.SmoothTransformation)
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(myScaledPixmap))
        self.setPalette(palette)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 50, 621, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border: 2px solid #ff9c10;\n"
"color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setLineWidth(2)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 260, 491, 551))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("border: 4px solid #ff9c10;")
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 220, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setLineWidth(2)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1370, 220, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setLineWidth(2)
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 830, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"      border: 2px solid #ff9c10;\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"       background-color: #ffffff; \n"
"      color: black;\n"
"    border: 0px solid #ff9c10;\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(840, 510, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"      border: 2px solid #ff9c10;\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"       background-color: #ffffff; \n"
"      color: black;\n"
"    border: 0px solid #ff9c10;\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(1260, 830, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border: 2px solid #ff9c10;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:5px;")
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(130, 160, 1641, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1210, 260, 491, 551))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("border: 4px solid #ff9c10;")
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(960, 200, 20, 281))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(960, 590, 20, 331))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        #self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        #self.progressBar.setGeometry(QtCore.QRect(660, 120, 601, 16))
        #self.progressBar.setRange(0,1)
        #font = QtGui.QFont()
        #font.setBold(False)
        #font.setWeight(50)
        #self.progressBar.setFont(font)
        #self.progressBar.setProperty("value", 0)
        #self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        #self.progressBar.setObjectName("progressBar")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(860, 940, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"      border: 2px solid Red;\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"       background-color: Red; \n"
"      color: white;\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setAutoDefault(True)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
#        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
#        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit_2 = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/ppt/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit_2.setIcon(icon)
        self.actionQuit_2.setObjectName("actionQuit_2")
        self.actionButtons = QtWidgets.QAction(MainWindow)
        self.actionButtons.setObjectName("actionButtons")
        self.actionAbout_us = QtWidgets.QAction(MainWindow)
        self.actionAbout_us.setObjectName("actionAbout_us")
        self.actionQuit_3 = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/ppt/quiit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit_3.setIcon(icon1)
        self.actionQuit_3.setObjectName("actionQuit_3")

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.showDialog)
        self.pushButton_2.clicked.connect(self.testCNN)
        self.pushButton_3.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:\\',"Image files (*.jpg *.gif)")
        imagePath = fname[0]
        img = cv2.imread(imagePath,1)
        cv2.imwrite('E:\\project\\minor project 2\\darkflow-master\\sample_img\\test.jpg',img)
        pixmap = QPixmap(imagePath)
        self.label_2.setPixmap(QPixmap(pixmap))
        
    def testCNN(self):
        test_image.main()
        imagePath = 'E:\\project\\minor project 2\\darkflow-master\\sample_img\\result.jpg'
        pixmap = QPixmap(imagePath)
        self.label_3.setPixmap(QPixmap(pixmap))
        text=open('E:\\project\minor project 2\\darkflow-master\\sample_img\\breedname.txt').read()
        self.textEdit.setPlainText(text)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "DOG DETECTOR"))
        self.label_4.setText(_translate("MainWindow", "INPUT"))
        self.label_5.setText(_translate("MainWindow", "OUTPUT"))
        self.pushButton.setText(_translate("MainWindow", "Import"))
        self.pushButton_2.setText(_translate("MainWindow", "DETECT"))
        self.pushButton_3.setText(_translate("MainWindow", "QUIT"))
        self.actionQuit.setText(_translate("MainWindow", "Open image"))
        self.actionQuit_2.setText(_translate("MainWindow", "Import image"))
        self.actionButtons.setText(_translate("MainWindow", "Buttons"))
        self.actionAbout_us.setText(_translate("MainWindow", "About us"))
        self.actionQuit_3.setText(_translate("MainWindow", "Quit"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())
