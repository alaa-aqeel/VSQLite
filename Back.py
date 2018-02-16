import sqlite3 as sqlite


class SQLite(sqlite.Connection):

	def __init__(self,dbname):
		super(SQLite,self).__init__(dbname)
		
	def getTable(self):
		cur = self.execute("SELECT name FROM sqlite_master WHERE type='table';")
		tables_list = []
		for i in cur.fetchall():
			tables_list.append(i[0])
		return tables_list
	def Isdb(self):
		try:
			self.execute("SELECT name FROM sqlite_master WHERE type='table';")
			return True
		except self.Error as er:
			return False


	def getColumns(self,table):
		cur = self.execute("PRAGMA table_info(%s);"%table).fetchall()
		cols_list = []
		for i in cur:
			cols_list.append(i[1])
		return cols_list


	def SortData(self,table):
		Columns   = self.execute("PRAGMA table_info(%s);"%table).fetchall()
		Info      = self.execute("select * from %s;"%table     ).fetchall()
		data_dict = {}
		for col in Columns:
			data_dict.update({col[1]:[]})
			for sel in Info:
				data_dict[col[1]].append(sel[Columns.index(col)])

		return data_dict