#!/usr/bin/env python3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from ui_mainwindow import Ui_MainWindow
import sys


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(QtWidgets.QMainWindow, self).__init__()

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ui = MainWindow()
	ui.show()
	sys.exit(app.exec_())
