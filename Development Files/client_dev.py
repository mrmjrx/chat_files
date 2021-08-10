# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text_viewer = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_viewer.setGeometry(QtCore.QRect(10, 0, 780, 500))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(16)
        self.text_viewer.setFont(font)
        self.text_viewer.setObjectName("text_viewer")
        self.text_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.text_entry.setGeometry(QtCore.QRect(10, 510, 680, 30))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(16)
        self.text_entry.setFont(font)
        self.text_entry.setText("")
        self.text_entry.setObjectName("text_entry")
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(690, 510, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")
        self.connection_label = QtWidgets.QLabel(self.centralwidget)
        self.connection_label.setGeometry(QtCore.QRect(10, 540, 780, 15))
        self.connection_label.setObjectName("connection_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReload_UI_Styling = QtWidgets.QAction(MainWindow)
        self.actionReload_UI_Styling.setObjectName("actionReload_UI_Styling")
        self.menuSettings.addAction(self.actionReload_UI_Styling)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.text_viewer.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'JetBrains Mono\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Server Text</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.connection_label.setText(_translate("MainWindow", "Connected to 255.255.255.255 as User"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionReload_UI_Styling.setText(_translate("MainWindow", "Reload UI Styling"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())