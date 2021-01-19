import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Fockus(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        uic.loadUi('1112.ui', self)
        self.pushButton.clicked.connect(self.new)

    def initUI(self):
        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle('Проект по яндекс Лицею')

    def new(self):
        name = self.lineEdit.text()
        self.lineEdit.setText(name)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Fockus()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
