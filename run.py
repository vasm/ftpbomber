#!/usr/bin/env python3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import sys

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	main_window = MainWindow()
	main_window.show()
	app.exec_()
