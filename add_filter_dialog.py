# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_filter.ui'
#
# Created: Tue Oct 14 11:36:18 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 147)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 10, 361, 91))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.chooseDimension = QtGui.QComboBox(self.widget)
        self.chooseDimension.setObjectName(_fromUtf8("chooseDimension"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.chooseDimension)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.chooseSign = QtGui.QComboBox(self.widget)
        self.chooseSign.setObjectName(_fromUtf8("chooseSign"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.chooseSign)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.chooseValue = QtGui.QComboBox(self.widget)
        self.chooseValue.setObjectName(_fromUtf8("chooseValue"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.chooseValue)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Dimension", None))
        self.label_2.setText(_translate("Dialog", "Sign", None))
        self.label_3.setText(_translate("Dialog", "Value", None))

