# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\HeroSoft\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(554, 329)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 70, 421, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.save_path_line = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.save_path_line.setObjectName("save_path_line")
        self.gridLayout.addWidget(self.save_path_line, 1, 1, 1, 1)
        self.chose_data_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.chose_data_btn.setObjectName("chose_data_btn")
        self.gridLayout.addWidget(self.chose_data_btn, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.chose_file_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.chose_file_btn.setObjectName("chose_file_btn")
        self.gridLayout.addWidget(self.chose_file_btn, 1, 2, 1, 1)
        self.handle_file_progress = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.handle_file_progress.setProperty("value", 0)
        self.handle_file_progress.setObjectName("handle_file_progress")
        self.gridLayout.addWidget(self.handle_file_progress, 2, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.data_path_line = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.data_path_line.setObjectName("data_path_line")
        self.gridLayout.addWidget(self.data_path_line, 0, 1, 1, 1)
        self.start_handle_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.start_handle_btn.setObjectName("start_handle_btn")
        self.gridLayout.addWidget(self.start_handle_btn, 3, 0, 1, 3)
        self.copy_sql_btn = QtWidgets.QPushButton(self.centralwidget)
        self.copy_sql_btn.setGeometry(QtCore.QRect(330, 240, 101, 21))
        self.copy_sql_btn.setObjectName("copy_sql_btn")
        self.open_link_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_link_btn.setGeometry(QtCore.QRect(440, 240, 101, 21))
        self.open_link_btn.setObjectName("open_link_btn")
        self.gen_pve_level_btn = QtWidgets.QCheckBox(self.centralwidget)
        self.gen_pve_level_btn.setGeometry(QtCore.QRect(330, 275, 241, 21))
        self.gen_pve_level_btn.setObjectName("gen_pve_level_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "英雄使用统计Excel生成器"))
        self.label.setText(_translate("MainWindow", "英雄数据路径"))
        self.save_path_line.setPlaceholderText(_translate("MainWindow", "请选择输出文件的路径"))
        self.chose_data_btn.setText(_translate("MainWindow", "选择"))
        self.label_4.setText(_translate("MainWindow", "文件处理进度"))
        self.chose_file_btn.setText(_translate("MainWindow", "选择"))
        self.handle_file_progress.setAccessibleDescription(_translate("MainWindow", "正在为您创建"))
        self.label_2.setText(_translate("MainWindow", "文件保存路径"))
        self.data_path_line.setPlaceholderText(_translate("MainWindow", "请选择英雄使用数据文件的路径"))
        self.start_handle_btn.setText(_translate("MainWindow", "开始"))
        self.copy_sql_btn.setText(_translate("MainWindow", "复制查询语句"))
        self.open_link_btn.setText(_translate("MainWindow", "打开查询网址"))
        self.gen_pve_level_btn.setText(_translate("MainWindow", "是否生成主城等级使用"))

