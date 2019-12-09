from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QImage, QPixmap
import cv2
from Ui_picshow import Ui_MainWindow
from lr_utils import load_dataset
from PyQt5 import QtCore, QtGui, QtWidgets

class picturezoom(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(picturezoom, self).__init__(parent)
        self.setupUi(self)

        self.line_edit.textChanged.connect(self.on_line_edit_textChanged)

        # self.connect(self.line_edit, QtCore.SIGNAL('textChanged()'), self, QtCore.SLOT('on_line_edit_changed()'))

    @pyqtSlot()
    def on_zoomin_clicked(self):
        """
        点击缩小图像
        """
        # TODO: not implemented yet
        self.zoomscale = self.zoomscale - 0.05
        if self.zoomscale <= 0:
            self.zoomscale = 0.2
        self.item.setScale(self.zoomscale)  # 缩小图像

    @pyqtSlot()
    def on_zoomout_clicked(self):
        """
        点击方法图像
        """
        # TODO: not implemented yet
        self.zoomscale = self.zoomscale + 0.05
        if self.zoomscale >= 1.2:
            self.zoomscale = 1.2
        self.item.setScale(self.zoomscale)  # 放大图像

    @pyqtSlot()
    def on_line_edit_textChanged(self):
        train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()
        index_str = self.line_edit.text()
        self.line_edit.setText(index_str)
        index = int(index_str)
        if(index < 0):
            index = 0
        img = train_set_x_orig[index]

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
        x = img.shape[1]  # 获取图像大小
        y = img.shape[0]
        self.zoomscale = 1  # 图片放缩尺度
        frame = QImage(img, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.picshow.setScene(self.scene)  # 将场景添加至视图




def main():
    import sys
    app = QApplication(sys.argv)
    piczoom = picturezoom()
    piczoom.show()
    app.exec_()


if __name__ == '__main__':
    main()