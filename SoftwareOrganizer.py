from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QInputDialog, QLineEdit, QLabel
from PyQt5.Qt import QIcon
from util.LoadFile import FileLoader
from math import ceil
from PyQt5.QtCore import pyqtSignal, Qt, QEvent
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath
import subprocess

"""
- Consider resizing labels with window
"""

categories_mode = True
file_open = False
key = 'categories'
add_button = {"icon": "plus_button.png", "exe": "Add Button"}
category_add_button = {"name": "Add Button", "icon": "plus_button.png"}
labels = []
window_title = 'Software Organizer by iBlitzkriegi'

file_loader = FileLoader()
data = file_loader.get_data()
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
        global categories_mode
        if len(items) == 0:
            items.append(add_button) if not categories_mode else items.append(category_add_button)
        row = 0
        column = 0
        special_key = 'exe' if not categories_mode else 'name'
        for item in items:
            label = IconLabel(self, file=item['icon'], window=self)
            labels.append(label)
            if 'Add Button' in item[special_key]:
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
        if file_loader.check_tutorial_mode('add-category'):
            QMessageBox.about(self, window_title, 'You will now be asked to give your new category a name.\n'
                                                  'This is just for storage mostly, so just give it a generic name\n'
                                                  'You will probably never see this name again, just make sure its unique!')
            file_loader.toggle_tutorial('add-category')
            file_loader.toggle_tutorial('first-open')
        text, ok = QInputDialog.getText(self, 'Get text', 'Category name:', QLineEdit.Normal, "")
        if not ok:
            return
        global file_open
        if file_loader.check_tutorial_mode('add-category-icon'):
            QMessageBox.about(self, window_title,
                              'Great! Now you will be asked to select an image to represent your new category.\n'
                              'Just browse to wherever your image is and select it. \n'
                              'It may be smart to pin an Icons folder to your Quick Access menu in windows explorer to make this process much faster!')
            file_loader.toggle_tutorial('add-category-icon')
        file_open = True
        icon, ok = QFileDialog.getOpenFileName(None, 'Select Icon File', '', 'Images (*.png *.jpg)')
        if not ok:
            file_open = False
            return
        global items
        global data
        items.append(
            {
                "name": text,
                "icon": icon
            }
        )
        data[text] = []
        self.clear_grid()
        file_loader.dump_data(data=data, items=items)
        global labels
        labels = []
        self.load_items()
        file_open = False
        self.setFocus(True)
        if file_loader.check_tutorial_mode('enter-category'):
            QMessageBox.about(self, window_title, 'And Ta-Daaaa! You have created a new category. \n'
                                                  'Now you can enter this category by left-clicking it. You can edit this category by right-clicking it!\n'
                                                  'To get back to the main category screen just click backspace at any time.')
            file_loader.toggle_tutorial('enter-category')

    def clear_grid(self):
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)

    def add_item(self):
        if file_loader.check_tutorial_mode('add-icon'):
            QMessageBox.about(self, window_title, 'This part is just like adding a category!\n'
                                                  'Select an image that represents this software.')
            file_loader.toggle_tutorial('add-icon')
        global file_open
        file_open = True
        icon, ok = QFileDialog.getOpenFileName(None, 'Select Icon File', '', 'Images (*.png *.jpg)')
        if not ok:
            file_open = False
            return
        if file_loader.check_tutorial_mode('add-game'):
            QMessageBox.about(self, window_title, 'This part however, is just a little different.\n'
                                                  'To add an executable, just find the .exe the software uses and select it.\n'
                                                  'If you are using this for say, setting up a game picker for steam, '
                                                  'then it is smart to pin your steamapps folder to your Quick Access menu in windows explorer to make this process much faster.')
            file_loader.toggle_tutorial('add-game')
        executable, ok = QFileDialog.getOpenFileName(None, 'Select Executable', '', 'Executable Files (*.exe)')
        if not ok:
            file_open = False
            return
        global items
        items.append(
            {
                "icon": icon,
                "exe": executable
            }
        )
        file_loader.dump_data(items=items)
        self.clear_grid()
        global labels
        labels = []
        file_open = False
        self.load_items()
        self.setFocus(True)


class IconLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, *args, file, window, antialiasing=True, **kwargs):
        super(IconLabel, self).__init__(*args, **kwargs)
        self.antialiasing = antialiasing
        self.window = window
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
        path.addRoundedRect(
            0, 0, self.width(), self.height(), self.radius, self.radius)

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, p)
        self.setPixmap(self.target)

    def mousePressEvent(self, e):
        self.clicked.emit()
        global file_open
        if file_open:
            return
        global labels
        global categories_mode
        global items
        clicked = [items[index] for index, label in enumerate(labels) if label == self]
        if len(clicked) == 0:
            return
        special_key = 'exe' if not categories_mode else 'name'
        if 'Add Button' in clicked[0][special_key]:
            return
        if e.type() == QEvent.MouseButtonPress:
            if e.button() == Qt.RightButton:
                pass
            else:
                if categories_mode:
                    labels = []
                    categories_mode = False
                    self.category_clicked(clicked)
                else:
                    self.item_clicked(clicked)

    def category_clicked(self, clicked):
        global items
        global data
        name = clicked[0]['name']
        data = file_loader.set_key(name)
        items = file_loader.get_items()
        self.window.clear_grid()
        self.window.load_items()

    def item_clicked(self, clicked):
        executable_name = [executable for executable in clicked[0]['exe'].split('/') if '.exe' in executable][0]
        directory = clicked[0]['exe'].replace(executable_name, '')
        subprocess.Popen([directory + executable_name], cwd=directory)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    if file_loader.is_first_open():
        reply = QMessageBox.question(window, window_title, 'Hello! Thank you for downloading my program!\n'
                                                           'Would you like me to show you tips on how to get started?')
        if reply == QMessageBox.No:
            file_loader.disable_tutorials()
        else:
            reply = QMessageBox.about(window, window_title,
                                      "This is the main screen. This is where your categories of software are stored.\n"
                                      "To create a new Category, click the + Icon.")
    sys.exit(app.exec_())
