# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.setEnabled(True)
        Form.resize(530, 494)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setAutoFillBackground(False)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.user_widget = QtWidgets.QWidget(Form)
        self.user_widget.setObjectName("user_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.user_widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left_close = QtWidgets.QPushButton(self.user_widget)
        self.left_close.setText("")
        self.left_close.setObjectName("left_close")
        self.horizontalLayout_2.addWidget(self.left_close)
        self.left_visit = QtWidgets.QPushButton(self.user_widget)
        self.left_visit.setText("")
        self.left_visit.setObjectName("left_visit")
        self.horizontalLayout_2.addWidget(self.left_visit)
        self.left_mini = QtWidgets.QPushButton(self.user_widget)
        self.left_mini.setText("")
        self.left_mini.setObjectName("left_mini")
        self.horizontalLayout_2.addWidget(self.left_mini)
        self.label = QtWidgets.QLabel(self.user_widget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.user_widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.user_widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.orientation = QtWidgets.QLineEdit(self.user_widget)
        self.orientation.setObjectName("orientation")
        self.verticalLayout_5.addWidget(self.orientation)
        self.destination = QtWidgets.QLineEdit(self.user_widget)
        self.destination.setObjectName("destination")
        self.verticalLayout_5.addWidget(self.destination)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.label_4 = QtWidgets.QLabel(self.user_widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.produce = QtWidgets.QPushButton(self.user_widget)
        self.produce.setObjectName("produce")
        self.horizontalLayout.addWidget(self.produce)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.output = QtWidgets.QTextBrowser(self.user_widget)
        self.output.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.output.setObjectName("output")
        self.verticalLayout_4.addWidget(self.output)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.user_widget, 0, 0, 1, 1)

        self.left_close.setFixedSize(10, 10)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(10, 10)  # 设置按钮大小
        self.left_mini.setFixedSize(10, 10)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.user_widget.setStyleSheet('''
    QWidget#user_widget{
        color:#232C51;
        background:white;
        border-top:1px solid darkGray;
        border-bottom:1px solid darkGray;
        border-right:1px solid darkGray;
        border-top-right-radius:10px;
        border-bottom-right-radius:10px;
        border-top-left-radius:10px;
        border-bottom-left-radius:10px;
    }''')
        self.output.setStyleSheet('''
    QTextBrowser#output{
        border-top-right-radius:10px;
        border-bottom-right-radius:10px;
        border-top-left-radius:10px;
        border-bottom-left-radius:10px;
    }''')
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "=============地铁票价生成&路径规划废物东西v好几.0============="))
        self.label_2.setText(_translate("Form", "起点"))
        self.label_3.setText(_translate("Form", "终点"))
        self.label_4.setText(_translate("Form", "若无终点输入则输出起点的票价表"))
        self.produce.setText(_translate("Form", "produce"))
        self.output.setHtml(_translate("Form",
                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                       "p, li { white-space: pre-wrap; }\n"
                                       "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                       "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))