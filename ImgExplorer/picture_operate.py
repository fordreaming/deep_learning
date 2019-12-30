from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QImage, QPixmap
from Ui_picshow import Ui_MainWindow
from lr_utils import load_dataset
import cv2

class picturezoom(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(picturezoom, self).__init__(parent)
        self.setupUi(self)
        self.zoomscale = 1                                      # 图片放缩尺度
        self.scene = QGraphicsScene()                           # 创建场景
        self.item = 0
        self.train_set_x_orig, self.train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()
        # self.line_edit.textChanged.connect(self.on_line_edit_textChanged)
        self.pushBtn.clicked.connect(self.on_line_edit_textChanged)

    @pyqtSlot()
    def on_zoomin_clicked(self):
        self.zoomscale = self.zoomscale - 0.05
        if self.zoomscale <= 0:
            self.zoomscale = 0.2
        self.item.setScale(self.zoomscale)  # 缩小图像

    @pyqtSlot()
    def on_zoomout_clicked(self):
        self.zoomscale = self.zoomscale + 0.05
        if self.zoomscale >= 1.2:
            self.zoomscale = 1.2
        self.item.setScale(self.zoomscale)  # 放大图像

    @pyqtSlot()
    def on_line_edit_textChanged(self):
        index_str = self.line_edit.text()
        self.line_edit.setText(index_str)
        index = int(index_str)
        total_img_num = self.train_set_y.shape[1]
        if index < 0:
            index = 0
        elif index > total_img_num:
            index = total_img_num
        img = self.train_set_x_orig[index]
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
        x = img.shape[1]                            # 获取图像大小
        y = img.shape[0]
        frame = QImage(img, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)        # 创建像素图元
        self.scene.removeItem(self.item)
        self.scene.addItem(self.item)
        self.picshow.setScene(self.scene)           # 将场景添加至视图

def main():
    import sys
    app = QApplication(sys.argv)
    piczoom = picturezoom()
    piczoom.show()
    app.exec_()


if __name__ == '__main__':
    main()