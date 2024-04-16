from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class ExampleWindow(QMainWindow):
    def __init__(self, windowsize):
        super().__init__()
        self.windowsize = windowsize
        self.initUI()

    def initUI(self):
        self.setFixedSize(self.windowsize)
        # self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)


        widget = QWidget()
        self.setCentralWidget(widget)

        # layout #
        layout_box = QHBoxLayout(widget)
        layout_box.setContentsMargins(0, 0, 0, 0)

        # image 1 #
        pixmap1 = QPixmap('docu/controllino_big.png')
        # pixmap1 = pixmap1.scaledToWidth(self.windowsize.width())
        self.image = QLabel()
        self.image.setPixmap(pixmap1)
        layout_box.addWidget(self.image)

        # # image 2 #
        pixmap2 = QPixmap('docu/controllino.png')
        self.image2 = QLabel(widget)
        self.image2.setPixmap(pixmap2)
        # self.image2.setFixedSize(pixmap2.size())

        # p = self.geometry().bottomRight() - self.image2.geometry().bottomRight() - QPoint(100, 100)
        # self.image2.move(p)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    size = QSize(1200,800)
    ex = ExampleWindow(size)
    ex.show()
    # screensize = app.desktop().availableGeometry().size()
    #
    # ex = ExampleWindow(screensize)
    # ex.show()

sys.exit(app.exec_())