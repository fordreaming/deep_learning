from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 200)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.grid_layout = QtWidgets.QGridLayout(self.centralWidget)
        self.grid_layout.setObjectName("grid_layout")

        self.grid_layout.setColumnStretch(0, 1)
        self.grid_layout.setColumnStretch(1, 4)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel()
        self.label.setObjectName("index")
        self.label.setText("index: ")

        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setObjectName("line_edit")

        self.pushBtn = QtWidgets.QPushButton()
        self.pushBtn.setObjectName("push button")
        self.pushBtn.setText("image show")

        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout.addWidget(self.line_edit)
        self.horizontalLayout.addWidget(self.pushBtn)

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
        MainWindow.setWindowTitle(_translate("MainWindow", "H5 image explore deep learning"))
        self.zoomout.setText(_translate("MainWindow", "zoom out"))
        self.zoomin.setText(_translate("MainWindow", "zoom in"))
