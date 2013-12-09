import sqlite3


class dbSqlite(db.db):
   
    def __ini__(self, host = "", username="", password="", db="", path="../../db/datamining.db"):
         self.conn = sqlite3.connect(path)

    def execute(self, qry="", data=[]):
         #execute query

    def insert(self, qry="", data=[]):
         self.conn.execute(qry, data)


        
     
