# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Oct 13 21:28:23 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("Apples application"))
        MainWindow.resize(421, 457)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.splitter = QtGui.QSplitter(self.centralWidget)
        self.splitter.setGeometry(QtCore.QRect(10, 20, 401, 391))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.chooseHorizontalDimension = QtGui.QComboBox(self.widget)
        self.chooseHorizontalDimension.setObjectName(_fromUtf8("chooseHorizontalDimension"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.chooseHorizontalDimension)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.chooseStorage = QtGui.QComboBox(self.widget)
        self.chooseStorage.setObjectName(_fromUtf8("chooseStorage"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.chooseStorage)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.chooseVerticalDimension = QtGui.QComboBox(self.widget)
        self.chooseVerticalDimension.setObjectName(_fromUtf8("chooseVerticalDimension"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.chooseVerticalDimension)
        self.filterTable = QtGui.QTableWidget(self.splitter)
        self.filterTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.filterTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.filterTable.setGridStyle(QtCore.Qt.SolidLine)
        self.filterTable.setObjectName(_fromUtf8("filterTable"))
        self.filterTable.setColumnCount(3)
        self.filterTable.setRowCount(0)
        self.filterTable.horizontalHeader().setResizeMode(1);
        item = QtGui.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(2, item)
        self.filterTable.horizontalHeader().setVisible(True)
        self.filterTable.horizontalHeader().setCascadingSectionResizes(False)
        self.filterTable.horizontalHeader().setStretchLastSection(False)
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.addButton = QtGui.QPushButton(self.widget1)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.horizontalLayout.addWidget(self.addButton)
        self.deleteButton = QtGui.QPushButton(self.widget1)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.horizontalLayout.addWidget(self.deleteButton)
        self.showButton = QtGui.QPushButton(self.widget1)
        self.showButton.setObjectName(_fromUtf8("showButton"))
        self.horizontalLayout.addWidget(self.showButton)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 421, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menuBar)
        #self.statusBar = QtGui.QStatusBar(MainWindow)
        #self.statusBar.setObjectName(_fromUtf8("statusBar"))
        #MainWindow.setStatusBar(self.statusBar)
        self.actionOpen_configuration = QtGui.QAction(MainWindow)
        self.actionOpen_configuration.setObjectName(_fromUtf8("actionOpen_configuration"))
        self.actionOpen_report = QtGui.QAction(MainWindow)
        self.actionOpen_report.setObjectName(_fromUtf8("actionOpen_report"))
        self.actionSave_report = QtGui.QAction(MainWindow)
        self.actionSave_report.setObjectName(_fromUtf8("actionSave_report"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionOpen_configuration)
        self.menuFile.addAction(self.actionOpen_report)
        self.menuFile.addAction(self.actionSave_report)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Apples application", None))
        self.label_3.setText(_translate("MainWindow", "Choose storage", None))
        self.label.setText(_translate("MainWindow", "Vertical dimension", None))
        self.label_2.setText(_translate("MainWindow", "Horizontal dimension", None))
        item = self.filterTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Dimension", None))
        item = self.filterTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Filter type", None))
        item = self.filterTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Value", None))
        self.addButton.setText(_translate("MainWindow", "Add filter", None))
        self.deleteButton.setText(_translate("MainWindow", "Delete filter", None))
        self.showButton.setText(_translate("MainWindow", "Build report", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionOpen_configuration.setText(_translate("MainWindow", "Open configuration", None))
        self.actionOpen_report.setText(_translate("MainWindow", "Open report", None))
        self.actionSave_report.setText(_translate("MainWindow", "Save report", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
