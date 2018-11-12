import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic

qt_file = "mainwindow.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_file)

class MyTable(QtWidgets.QMainWindow, Ui_MainWindow):
	"""docstring for MyTable"""
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.pushButton.clicked.connect(self.solve_sudoku)
	def solve_sudoku(self):
		box = []
		if self.b11.toPlainText():
			box.append(self.b11.toPlainText())
		else:
			box.append('0')
		if self.b12.toPlainText():
			box.append(self.b12.toPlainText())
		else:
			box.append('0')
		if self.b13.toPlainText():
			box.append(self.b13.toPlainText())
		else:
			box.append('0')
		if self.b14.toPlainText():
			box.append(self.b14.toPlainText())
		else:
			box.append('0')
		if self.b15.toPlainText():
			box.append(self.b15.toPlainText())
		else:
			box.append('0')
		if self.b16.toPlainText():
			box.append(self.b16.toPlainText())
		else:
			box.append('0')
		if self.b17.toPlainText():
			box.append(self.b17.toPlainText())
		else:
			box.append('0')
		if self.b18.toPlainText():
			box.append(self.b18.toPlainText())
		else:
			box.append('0')
		if self.b19.toPlainText():
			box.append(self.b19.toPlainText())
		else:
			box.append('0')
		if self.b21.toPlainText():
			box.append(self.b21.toPlainText())
		else:
			box.append('0')
		if self.b22.toPlainText():
			box.append(self.b22.toPlainText())
		else:
			box.append('0')
		if self.b23.toPlainText():
			box.append(self.b23.toPlainText())
		else:
			box.append('0')
		if self.b24.toPlainText():
			box.append(self.b24.toPlainText())
		else:
			box.append('0')
		if self.b25.toPlainText():
			box.append(self.b25.toPlainText())
		else:
			box.append('0')
		if self.b26.toPlainText():
			box.append(self.b26.toPlainText())
		else:
			box.append('0')
		if self.b27.toPlainText():
			box.append(self.b27.toPlainText())
		else:
			box.append('0')
		if self.b28.toPlainText():
			box.append(self.b28.toPlainText())
		else:
			box.append('0')
		if self.b29.toPlainText():
			box.append(self.b29.toPlainText())
		else:
			box.append('0')
		if self.b31.toPlainText():
			box.append(self.b31.toPlainText())
		else:
			box.append('0')
		if self.b32.toPlainText():
			box.append(self.b32.toPlainText())
		else:
			box.append('0')
		if self.b33.toPlainText():
			box.append(self.b33.toPlainText())
		else:
			box.append('0')
		if self.b34.toPlainText():
			box.append(self.b34.toPlainText())
		else:
			box.append('0')
		if self.b35.toPlainText():
			box.append(self.b35.toPlainText())
		else:
			box.append('0')
		if self.b36.toPlainText():
			box.append(self.b36.toPlainText())
		else:
			box.append('0')
		if self.b37.toPlainText():
			box.append(self.b37.toPlainText())
		else:
			box.append('0')
		if self.b38.toPlainText():
			box.append(self.b38.toPlainText())
		else:
			box.append('0')
		if self.b39.toPlainText():
			box.append(self.b39.toPlainText())
		else:
			box.append('0')
		if self.b41.toPlainText():
			box.append(self.b41.toPlainText())
		else:
			box.append('0')
		if self.b42.toPlainText():
			box.append(self.b42.toPlainText())
		else:
			box.append('0')
		if self.b43.toPlainText():
			box.append(self.b43.toPlainText())
		else:
			box.append('0')
		if self.b44.toPlainText():
			box.append(self.b44.toPlainText())
		else:
			box.append('0')
		if self.b45.toPlainText():
			box.append(self.b45.toPlainText())
		else:
			box.append('0')
		if self.b46.toPlainText():
			box.append(self.b46.toPlainText())
		else:
			box.append('0')
		if self.b47.toPlainText():
			box.append(self.b47.toPlainText())
		else:
			box.append('0')
		if self.b48.toPlainText():
			box.append(self.b48.toPlainText())
		else:
			box.append('0')
		if self.b49.toPlainText():
			box.append(self.b49.toPlainText())
		else:
			box.append('0')
		if self.b51.toPlainText():
			box.append(self.b51.toPlainText())
		else:
			box.append('0')
		if self.b52.toPlainText():
			box.append(self.b52.toPlainText())
		else:
			box.append('0')
		if self.b53.toPlainText():
			box.append(self.b53.toPlainText())
		else:
			box.append('0')
		if self.b54.toPlainText():
			box.append(self.b54.toPlainText())
		else:
			box.append('0')
		if self.b55.toPlainText():
			box.append(self.b55.toPlainText())
		else:
			box.append('0')
		if self.b56.toPlainText():
			box.append(self.b56.toPlainText())
		else:
			box.append('0')
		if self.b57.toPlainText():
			box.append(self.b57.toPlainText())
		else:
			box.append('0')
		if self.b58.toPlainText():
			box.append(self.b58.toPlainText())
		else:
			box.append('0')
		if self.b59.toPlainText():
			box.append(self.b59.toPlainText())
		else:
			box.append('0')
		if self.b61.toPlainText():
			box.append(self.b61.toPlainText())
		else:
			box.append('0')
		if self.b62.toPlainText():
			box.append(self.b62.toPlainText())
		else:
			box.append('0')
		if self.b63.toPlainText():
			box.append(self.b63.toPlainText())
		else:
			box.append('0')
		if self.b64.toPlainText():
			box.append(self.b64.toPlainText())
		else:
			box.append('0')
		if self.b65.toPlainText():
			box.append(self.b65.toPlainText())
		else:
			box.append('0')
		if self.b66.toPlainText():
			box.append(self.b66.toPlainText())
		else:
			box.append('0')
		if self.b67.toPlainText():
			box.append(self.b67.toPlainText())
		else:
			box.append('0')
		if self.b68.toPlainText():
			box.append(self.b68.toPlainText())
		else:
			box.append('0')
		if self.b69.toPlainText():
			box.append(self.b69.toPlainText())
		else:
			box.append('0')
		if self.b71.toPlainText():
			box.append(self.b71.toPlainText())
		else:
			box.append('0')
		if self.b72.toPlainText():
			box.append(self.b72.toPlainText())
		else:
			box.append('0')
		if self.b73.toPlainText():
			box.append(self.b73.toPlainText())
		else:
			box.append('0')
		if self.b74.toPlainText():
			box.append(self.b74.toPlainText())
		else:
			box.append('0')
		if self.b75.toPlainText():
			box.append(self.b75.toPlainText())
		else:
			box.append('0')
		if self.b76.toPlainText():
			box.append(self.b76.toPlainText())
		else:
			box.append('0')
		if self.b77.toPlainText():
			box.append(self.b77.toPlainText())
		else:
			box.append('0')
		if self.b78.toPlainText():
			box.append(self.b78.toPlainText())
		else:
			box.append('0')
		if self.b79.toPlainText():
			box.append(self.b79.toPlainText())
		else:
			box.append('0')
		if self.b81.toPlainText():
			box.append(self.b81.toPlainText())
		else:
			box.append('0')
		if self.b82.toPlainText():
			box.append(self.b82.toPlainText())
		else:
			box.append('0')
		if self.b83.toPlainText():
			box.append(self.b83.toPlainText())
		else:
			box.append('0')
		if self.b84.toPlainText():
			box.append(self.b84.toPlainText())
		else:
			box.append('0')
		if self.b85.toPlainText():
			box.append(self.b85.toPlainText())
		else:
			box.append('0')
		if self.b86.toPlainText():
			box.append(self.b86.toPlainText())
		else:
			box.append('0')
		if self.b87.toPlainText():
			box.append(self.b87.toPlainText())
		else:
			box.append('0')
		if self.b88.toPlainText():
			box.append(self.b88.toPlainText())
		else:
			box.append('0')
		if self.b89.toPlainText():
			box.append(self.b89.toPlainText())
		else:
			box.append('0')
		if self.b91.toPlainText():
			box.append(self.b91.toPlainText())
		else:
			box.append('0')
		if self.b92.toPlainText():
			box.append(self.b92.toPlainText())
		else:
			box.append('0')
		if self.b93.toPlainText():
			box.append(self.b93.toPlainText())
		else:
			box.append('0')
		if self.b94.toPlainText():
			box.append(self.b94.toPlainText())
		else:
			box.append('0')
		if self.b95.toPlainText():
			box.append(self.b95.toPlainText())
		else:
			box.append('0')
		if self.b96.toPlainText():
			box.append(self.b96.toPlainText())
		else:
			box.append('0')
		if self.b97.toPlainText():
			box.append(self.b97.toPlainText())
		else:
			box.append('0')
		if self.b98.toPlainText():
			box.append(self.b98.toPlainText())
		else:
			box.append('0')
		if self.b99.toPlainText():
			box.append(self.b99.toPlainText())
		else:
			box.append('0')
		box = " ".join(str(x) for x in box)
		self.output.setText(box)
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = MyTable()
	window.show()
	sys.exit(app.exec_())
