from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 200)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.grid_layout = QtWidgets.QGridLayout(self.centralWidget)
        self.grid_layout.setObjectName("grid_layout")

        # //设置第一列和第二列的比例
        self.grid_layout.setColumnStretch(0, 1)
        self.grid_layout.setColumnStretch(1, 4)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel()
        self.label.setObjectName("index")
        self.label.setText("index: ")

        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setObjectName("line_edit")

        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout.addWidget(self.line_edit)

        self.grid_layout.addLayout(self.horizontalLayout, 0, 0)

        self.zoomout = QtWidgets.QPushButton()
        self.zoomout.setObjectName("zoomout")
        self.grid_layout.addWidget(self.zoomout, 1, 0)
        #
        self.zoomin = QtWidgets.QPushButton()
        self.zoomin.setObjectName("zoomin")
        self.grid_layout.addWidget(self.zoomin, 2, 0)

        self.picshow = QtWidgets.QGraphicsView()
        self.picshow.setObjectName("picshow")
        self.grid_layout.addWidget(self.picshow, 0, 1, 4, 1)

        MainWindow.setCentralWidget(self.centralWidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "H5图像浏览器——神经网络和深度学习 - 第二周作业"))
        self.zoomout.setText(_translate("MainWindow", "放大"))
        self.zoomin.setText(_translate("MainWindow", "缩小"))
