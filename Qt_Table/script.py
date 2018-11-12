import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.title = 'PyQt5 table Sudoku'
		self.left = 0
		self.top = 0
		self.width = 600
		self.height = 600
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.createTable()

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.tableWidget)
		self.setLayout(self.layout)

		self.show()

	def createTable(self):
		self.tableWidget = QTableWidget()
		self.tableWidget.setRowCount(9)
		self.tableWidget.setColumnCount(9)
		self.tableWidget.setItem(0,0, QTableWidgetItem("0.0"))
		self.tableWidget.setItem(2,2, QTableWidgetItem("2.2"))
		self.tableWidget.setItem(4,4, QTableWidgetItem("4.4"))
		self.tableWidget.setItem(6,6, QTableWidgetItem("6.6"))
		self.tableWidget.move(0,0)

		self.tableWidget.doubleClicked.connect(self.on_click)

	@pyqtSlot()
	def on_click(self):
		print("\n")
		for currentQTableWidgetItem in self.tableWidget.selectedItems():
			print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec())