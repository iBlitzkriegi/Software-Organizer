from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal


class IconLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.setText('Testtt')
