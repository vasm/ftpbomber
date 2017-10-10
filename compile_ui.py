#!/usr/bin/env python3
from PyQt5.uic import compileUi


ui_files = [('mainwindow.ui', 'ui_mainwindow.py')]


if __name__ == '__main__':
	for ui_file in ui_files:
		with open(ui_file[1], 'w') as output:
			compileUi(ui_file[0], output)
