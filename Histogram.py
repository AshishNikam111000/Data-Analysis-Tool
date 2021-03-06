# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Histogram.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Hist(object):
    def setupUi(self, Hist):
        Hist.setObjectName("Hist")
        Hist.resize(326, 228)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Hist.sizePolicy().hasHeightForWidth())
        Hist.setSizePolicy(sizePolicy)
        Hist.setStyleSheet("border-image: url(:/images/BackGround.jpg);")
        self.gridLayout = QtWidgets.QGridLayout(Hist)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Hist)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Hist)
        self.comboBox.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Hist)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(Hist)
        self.comboBox_2.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.comboBox_2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Hist)
        self.buttonBox.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Hist)
        self.buttonBox.accepted.connect(Hist.accept)
        self.buttonBox.rejected.connect(Hist.reject)
        QtCore.QMetaObject.connectSlotsByName(Hist)

    def retranslateUi(self, Hist):
        _translate = QtCore.QCoreApplication.translate
        Hist.setWindowTitle(_translate("Hist", "Histogram"))
        self.label.setText(_translate("Hist", "<html><head/><body><p><span style=\" color:#ffffff;\">Select the Feature Column : </span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Hist", "SELECT"))
        self.label_2.setText(_translate("Hist", "<html><head/><body><p><span style=\" color:#ffffff;\">Select the  Column  : </span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("Hist", "SELECT"))
import Images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Hist = QtWidgets.QDialog()
    ui = Ui_Hist()
    ui.setupUi(Hist)
    Hist.show()
    sys.exit(app.exec_())
