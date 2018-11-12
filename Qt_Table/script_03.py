import sys

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QTableWidget
from PySide2.QtCore import QFIle, QObject

class Form(QObject):
	"""docstring for Form"""
	def __init__(self, ui_file,parent=None):
		super(Form, self).__init__(parent)
		ui_file = QFIle(ui_file)
		ui_file.open(QFIle.ReadOnly)

		loader = QUiLoader()
		self.window = loader.load(ui_file)
		ui_file.close()

		# self.line = self.window.findChild(QLineEdit, 'lineEdit')

		btn = self.window.findChild(QPushButton, 'solve')
		btn.clicked.connect(self.solver)
		self.window.show()

	def solver(self):
		print("Push button pressed")

if __name__ == '__main__':
	app = QApplication(sys.argv)
	form = Form('qt_table.ui')
	sys.exit(app.exec_())
		