import sys
from PIL import Image
from PIL import ImageDraw
from random import randrange

from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        im = Image.new('RGBA', (580, 351), (256, 256, 256))
        draw = ImageDraw.Draw(im)

        for i in range(randrange(10)):
            x, y = randrange(580), randrange(351)
            r = randrange(50)
            draw.ellipse((x - r, y - r, x + r, y + r), 'yellow')

        data = im.tobytes('raw', 'RGBA')
        qim = QImage(data, im.size[0], im.size[1], QImage.Format_RGBA8888)

        pix = QPixmap(qim)
        self.label.setPixmap(pix)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
