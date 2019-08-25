from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QInputDialog, QLineEdit, QLabel
from PyQt5.Qt import QIcon
from util.LoadFile import FileLoader
from math import ceil
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath
import json

"""
- Setup label to scale images to 96, 96
"""

categories_mode = True
file_open = False
key = 'categories'
add_button = {"icon": "plus_button.png", "exe": "Add Button"}
category_add_button = {"name": "Add Button", "icon": "plus_button.png"}
labels = []
window_title = 'Software Organizer by iBlitzkriegi'

file_loader = FileLoader()
items = file_loader.get_items()


class Ui_SoftwareIOrganizer(object):
    def setupUi(self, SoftwareIOrganizer):
        SoftwareIOrganizer.setObjectName("SoftwareIOrganizer")
        SoftwareIOrganizer.resize(476, 295)
        self.centralwidget = QtWidgets.QWidget(SoftwareIOrganizer)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout.addLayout(self.gridLayout)
        SoftwareIOrganizer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SoftwareIOrganizer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 21))
        self.menubar.setObjectName("menubar")
        SoftwareIOrganizer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SoftwareIOrganizer)
        self.statusbar.setObjectName("statusbar")
        SoftwareIOrganizer.setStatusBar(self.statusbar)

        self.retranslateUi(SoftwareIOrganizer)
        QtCore.QMetaObject.connectSlotsByName(SoftwareIOrganizer)

    def retranslateUi(self, SoftwareIOrganizer):
        _translate = QtCore.QCoreApplication.translate
        SoftwareIOrganizer.setWindowTitle(_translate("SoftwareIOrganizer", window_title))


class MainWindow(QMainWindow, Ui_SoftwareIOrganizer):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setMaximumWidth(110 * 4)
        self.setMinimumWidth(110 * 4)
        self.setFixedHeight(135)
        self.setWindowIcon(QIcon('Icon.png'))
        self.setupUi(self)
        self.load_items()

    def load_items(self):
        if len(items) == 0:
            items.append(add_button) if not categories_mode else items.append(category_add_button)
        row = 0
        column = 0
        special_key = 'icon' if not categories_mode else 'name'
        for item in items:
            label = IconLabel(self, file=item['icon'], window=self)
            labels.append(label)
            if 'Add Button' in item[special_key]:
                print('IT IS')
                label.clicked.connect(self.add_item if not categories_mode else self.add_category)
            self.gridLayout.addWidget(label, row, column, 1, 1)
            if column + 1 == 4:
                row += 1
                column = 0
            else:
                column += 1
        row = ceil(len(items) / 4)
        self.setFixedHeight(125 * row)
        file_loader.dump_data(items=items)

    def add_category(self):
        text, ok = QInputDialog.getText(self, 'Get text', 'Category name:', QLineEdit.Normal, "")
        if not ok:
            return

        print('Adding category')

    def add_item(self):
        print('ADSDADA')


class IconLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, *args, file, window, antialiasing=True, **kwargs):
        super(IconLabel, self).__init__(*args, **kwargs)
        self.antialiasing = antialiasing
        self.window = window
        print(file)
        self.file = file
        self.setMaximumSize(96, 96)
        self.setMinimumSize(96, 96)
        self.radius = 96

        self.target = QPixmap(self.size())
        self.target.fill(Qt.transparent)

        p = QPixmap(self.file).scaled(
            96, 96, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        painter = QPainter(self.target)
        if self.antialiasing:
            painter.setRenderHint(QPainter.Antialiasing, True)
            painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
            painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        path = QPainterPath()
        print(self.width())
        path.addRoundedRect(
            0, 0, self.width(), self.height(), self.radius, self.radius)

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, p)
        self.setPixmap(self.target)

    def mousePressEvent(self, e):
        self.clicked.emit()


if __name__ == "__main__":
    import sys

    # TODO Create a welcome tutorial with basic walkthrough with file_loader.is_first_open()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # if file_loader.is_first_open():
    #     reply = QMessageBox.question(window, window_title, 'Hello! Thank you for downloading my program!\n'
    #                                                        'Would you like me to show you tips on how to get started?')
    #     if reply == QMessageBox.No:
    #         file_loader.disable_tutorials()
    sys.exit(app.exec_())
