from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(600, 300))
        MainWindow.setMaximumSize(QtCore.QSize(600, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.isim = QtWidgets.QLabel(self.centralwidget)
        self.isim.setGeometry(QtCore.QRect(70, 90, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.isim.setFont(font)
        self.isim.setObjectName("isim")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 90, 301, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 140, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.klasor_ac)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 140, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.cevir)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 190, 111, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def klasor_ac(self):
        self.klasor_yolu, _ = QFileDialog.getOpenFileName(filter="*.ui")

    def cevir(self):
        if self.lineEdit.text() == "" or self.klasor_yolu == "":
            self.label.setText("İsim veya dosya Girmediniz...")
        else:
            yol = self.klasor_yolu.split("/")
            dosya_adi = yol[-1]
            isim = self.lineEdit.text()
            yol.remove(dosya_adi)
            klasor_yolu = str("//".join(yol))
            os.chdir(klasor_yolu)
            os.system('pyuic5 ' + dosya_adi + ' -o ' + isim + '.py')
            self.label.setText("Dönüştürüldü...")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.isim.setText(_translate("MainWindow", "İsim Giriniz :"))
        self.pushButton.setText(_translate("MainWindow", "Dosyayı Bul"))
        self.pushButton_2.setText(_translate("MainWindow", "Çevir"))


app = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()
sys.exit(app.exec_())
