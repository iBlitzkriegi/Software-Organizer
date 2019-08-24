from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.Qt import QIcon
from util.LoadFile import FileLoader
from util.IconLabels import IconLabel
import json

file_loader = FileLoader()
categories_mode = True
key = 'categories'
add_button = {"icon": "plus_button.png", "exe": "Add Button"}
category_add_button = {"name": "Add Button", "icon": "plus_button.png"}
labels = []
window_title = 'Software Organizer by iBlitzkriegi'
data = file_loader.load_file()
items = file_loader.get_items()
file_loader.dump_data(items, data=data)



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

if __name__ == "__main__":
    import sys
    #TODO Create a welcome tutorial with basic walkthrough with file_loader.is_first_open()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    if file_loader.is_first_open():
        reply = QMessageBox.question(window, window_title, 'Hello! Thank you for downloading my program!\n'
                                                'Would you like me to show you tips on how to get started?')
        if reply == QMessageBox.No:
            file_loader.disable_tutorials()
    sys.exit(app.exec_())
