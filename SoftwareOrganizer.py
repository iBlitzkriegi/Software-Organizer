from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.Qt import QIcon
from util.LoadFile import FileLoader
import json

file_loader = FileLoader()
categories_mode = True
key = 'categories'
add_button = {"icon": "plus_button.png", "exe": "Add Button"}
category_add_button = {"name": "Add Button", "icon": "plus_button.png"}
labels = []
data = file_loader.load_file()



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
        SoftwareIOrganizer.setWindowTitle(_translate("SoftwareIOrganizer", "Software Organizer by iBlitzkriegi"))


class MainWindow(QMainWindow, Ui_SoftwareIOrganizer):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.resize(110, 135)
        self.setWindowIcon(QIcon('Icon.png'))
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    #TODO Create a welcome tutorial with basic walkthrough with file_loader.is_first_open()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
