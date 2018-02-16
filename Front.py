from PyQt5.QtWidgets import ( 
								QMainWindow,QWidget,QApplication,
								QVBoxLayout,QAction,QFileDialog,qApp,
								QTableWidget,QListWidget,QSplitter,
								QTableWidgetItem,QMessageBox
					)

from PyQt5.QtCore import Qt
from PyQt5.QtGui  import QIcon,QFont
from Back        import SQLite
import os 

class VSQLite(QMainWindow):


	def __init__(self,p=None):
		super(VSQLite,self).__init__()

		#Widgets & layout
		inset = QWidget()
		vbox  = QVBoxLayout(inset) 
		self.split = Spliter()

		self.setStyleSheet(open("static/style.css","r").read())

		#Tools Widgets
		self.table = Table (self)
		self.lists = List  (self)

		#add 
		self.split.add(self.lists)
		self.split.add(self.table)
		self.split.size(10,300)
		vbox.addWidget(self.split)


		# QMainWindow ( self )
		self.setCentralWidget(inset)
		self.resize(700,500)
		self.setMinimumWidth(600)
		self.setWindowTitle("SQLIte")
		self.setWindowIcon(QIcon("static/imgs/database.svg"))
		# self.split


		#QMnueBar
		toolsBar    = self.addToolBar("Main")
	

		odbite      = QAction(QIcon(os.getcwd()+"/static/imgs/file-2.svg"),"Open",self,triggered=self.Open)
		toolsBar.addAction(odbite)

		if p:
			self.OpenSQLite(p)


	def Open(self):
		path ,ext = QFileDialog.getOpenFileName(self,"Open sqlite","","sqlite(*.db *.sql *.sqlite *sqlite3)")
		if path.strip() != "":
			self.OpenSQLite(path)

	def OpenSQLite(self,p):

			self.lists.clear()
			self.table.clear()

			self.sql = SQLite(p)
			if self.sql.Isdb():

				self.addCol = lambda item:self.table.setd(self.sql,item.text())
				self.lists.setTables(self.sql.getTable())
				self.lists.itemActivated.connect(self.addCol)
				self.lists.itemClicked.connect(self.addCol)
				self.setWindowTitle("%s-VSQLite"%p)

			else:
				MessageBox("file is Not Database",self)



class MessageBox(QMessageBox):

	def __init__(self,text,main=None):
		super(MessageBox,self).__init__(main)

		self.setText(text)
		self.setWindowTitle("Error SQlite")
		self.setToolTip("Error SQLite ...")
		self.setIcon(self.Warning)
		self.setStyleSheet("QLabel{ font-size:16px;font-family:Chandas }")
		self.setStandardButtons(self.Ok)
		self.show()

		

class Table(QTableWidget):

	def __init__(self,p=None):
		super(Table,self).__init__(p)

		self.setRowCount(10)
		self.setColumnCount(5)



	def setd(self,sql,table):
		self.setRowCount(0)
		cols = sql.getColumns(table)
		dbs  = sql.SortData(table)
		self.setColumnCount(len(cols))
		
		for col in cols:
			self.setHorizontalHeaderItem(cols.index(col),QTableWidgetItem(col))

			self.setColumnWidth(cols.index(col),len(col)*30)
			for db in dbs[col]:
				self.setRowCount(len(dbs[col]))
				item = QTableWidgetItem(str(db))
				item.setTextAlignment(Qt.AlignCenter)
				
				item.setFont(QFont("Chandas",13))
				self.setItem(dbs[col].index(db),cols.index(col),item)


				self.setRowHeight(dbs[col].index(db),30)
			

class List(QListWidget):

	def __init__(self,p=None):
		super(List,self).__init__(p)	
		self.setFont(QFont("gargi",12))

	def setTables(self,tables):
		for i in tables:
			self.addItem(i)


class Spliter(QSplitter):

	def __init__(self,p=None):
		super(Spliter,self).__init__(p)

	def add(self,widget):

		self.addWidget(widget)

	def size(self,*sizes):

		self.setSizes(list(sizes))