# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\_activity\_programming\_projects\_sushi_calc\window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(262, 299)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\_activity\\_programming\\_projects\\_sushi_calc\\Favourite2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.let_rice_val = QtWidgets.QLineEdit(self.centralwidget)
        self.let_rice_val.setGeometry(QtCore.QRect(10, 30, 113, 22))
        self.let_rice_val.setObjectName("let_rice_val")
        self.lbl_rice_val = QtWidgets.QLabel(self.centralwidget)
        self.lbl_rice_val.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.lbl_rice_val.setObjectName("lbl_rice_val")
        self.lbl_acid_val = QtWidgets.QLabel(self.centralwidget)
        self.lbl_acid_val.setGeometry(QtCore.QRect(140, 10, 53, 16))
        self.lbl_acid_val.setObjectName("lbl_acid_val")
        self.let_acid_val = QtWidgets.QLineEdit(self.centralwidget)
        self.let_acid_val.setGeometry(QtCore.QRect(140, 30, 113, 22))
        self.let_acid_val.setReadOnly(True)
        self.let_acid_val.setObjectName("let_acid_val")
        self.lbl_shugar_val = QtWidgets.QLabel(self.centralwidget)
        self.lbl_shugar_val.setGeometry(QtCore.QRect(140, 60, 53, 16))
        self.lbl_shugar_val.setObjectName("lbl_shugar_val")
        self.let_shugar_val = QtWidgets.QLineEdit(self.centralwidget)
        self.let_shugar_val.setGeometry(QtCore.QRect(140, 80, 113, 22))
        self.let_shugar_val.setReadOnly(True)
        self.let_shugar_val.setObjectName("let_shugar_val")
        self.let_water_val = QtWidgets.QLineEdit(self.centralwidget)
        self.let_water_val.setGeometry(QtCore.QRect(140, 180, 113, 22))
        self.let_water_val.setReadOnly(True)
        self.let_water_val.setObjectName("let_water_val")
        self.let_salt_val = QtWidgets.QLineEdit(self.centralwidget)
        self.let_salt_val.setGeometry(QtCore.QRect(140, 130, 113, 22))
        self.let_salt_val.setReadOnly(True)
        self.let_salt_val.setObjectName("let_salt_val")
        self.lbl_water_val = QtWidgets.QLabel(self.centralwidget)
        self.lbl_water_val.setGeometry(QtCore.QRect(140, 160, 53, 16))
        self.lbl_water_val.setObjectName("lbl_water_val")
        self.lbl_salt_val = QtWidgets.QLabel(self.centralwidget)
        self.lbl_salt_val.setGeometry(QtCore.QRect(140, 110, 53, 16))
        self.lbl_salt_val.setObjectName("lbl_salt_val")
        self.let_total_sushu_cnt = QtWidgets.QLineEdit(self.centralwidget)
        self.let_total_sushu_cnt.setGeometry(QtCore.QRect(140, 230, 113, 22))
        self.let_total_sushu_cnt.setReadOnly(True)
        self.let_total_sushu_cnt.setObjectName("let_total_sushu_cnt")
        self.lbl_total_sushu_cnt = QtWidgets.QLabel(self.centralwidget)
        self.lbl_total_sushu_cnt.setGeometry(QtCore.QRect(140, 210, 121, 16))
        self.lbl_total_sushu_cnt.setObjectName("lbl_total_sushu_cnt")
        self.lbl_rice_per_sushi = QtWidgets.QLabel(self.centralwidget)
        self.lbl_rice_per_sushi.setGeometry(QtCore.QRect(10, 60, 111, 16))
        self.lbl_rice_per_sushi.setObjectName("lbl_rice_per_sushi")
        self.let_rice_per_sushi = QtWidgets.QLineEdit(self.centralwidget)
        self.let_rice_per_sushi.setGeometry(QtCore.QRect(10, 80, 113, 22))
        self.let_rice_per_sushi.setObjectName("let_rice_per_sushi")
        self.pbn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pbn_reset.setGeometry(QtCore.QRect(10, 120, 111, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\_activity\\_programming\\_projects\\_sushi_calc\\Interdit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbn_reset.setIcon(icon1)
        self.pbn_reset.setObjectName("pbn_reset")
        self.pbn_calc = QtWidgets.QPushButton(self.centralwidget)
        self.pbn_calc.setGeometry(QtCore.QRect(10, 190, 111, 61))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\_activity\\_programming\\_projects\\_sushi_calc\\Tips.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbn_calc.setIcon(icon2)
        self.pbn_calc.setObjectName("pbn_calc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 262, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SushiCalc"))
        self.lbl_rice_val.setText(_translate("MainWindow", "Количество риса"))
        self.lbl_acid_val.setText(_translate("MainWindow", "Уксус"))
        self.lbl_shugar_val.setText(_translate("MainWindow", "Сахар"))
        self.lbl_water_val.setText(_translate("MainWindow", "Вода"))
        self.lbl_salt_val.setText(_translate("MainWindow", "Соль"))
        self.lbl_total_sushu_cnt.setText(_translate("MainWindow", "Количество роллов"))
        self.lbl_rice_per_sushi.setText(_translate("MainWindow", "Рис на 1 ролл"))
        self.pbn_reset.setText(_translate("MainWindow", "Сброс"))
        self.pbn_reset.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.pbn_calc.setText(_translate("MainWindow", "Рассчитать"))
        self.pbn_calc.setShortcut(_translate("MainWindow", "Return"))
