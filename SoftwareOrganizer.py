from PyQt5 import QtCore, QtGui, QtWidgets


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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    SoftwareIOrganizer = QtWidgets.QMainWindow()
    ui = Ui_SoftwareIOrganizer()
    ui.setupUi(SoftwareIOrganizer)
    SoftwareIOrganizer.show()
    sys.exit(app.exec_())
