import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

qtCreatorFile = "qt_table.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class SudokuApp(QtWidgets.QMainWindow,QtWidgets.QTableWidget, Ui_MainWindow):
	"""docstring for SudokuApp"""
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		QtWidgets.QTableWidget.__init__(self)
		self.setupUi(self)
		# self.table = QTableWidget()
		for i in range(9):
			for j in range(9):
				self.setItem(i,j, QTableWidgetItem(i))
	# 	self.solve.clicked.connect(self.getInput)
	# def getInput(self):
	# 	for i in range(9):
	# 		for j in range(9):
	# 			self.getItem(i,j, QTableWidgetItem(i))


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = SudokuApp()
	window.show()
	sys.exit(app.exec_())
