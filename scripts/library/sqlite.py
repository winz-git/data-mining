#!/usr/bin/env python3

import sqlite3
import os, sys

from library.db import db

class dbSqlite(db):
   
    conn = None
    cur = None
   
    def __init__(self, host = "", username="", password="", db="", path="../../db/datamining.db"):
         """ verify file """
         if(os.path.isfile(path)):
             try:
                 self.conn = sqlite3.connect(path)
                 
                 self.cur = self.conn.cursor()
                                  
             except Exception as e:
                 print("Connection error", e)
                 sys.exit(1)
                 
         else:
             print("Failed to locate db", path)

    def execute(self, qry="", data=[]):
                  
         if(len(data) == 0):
             self.cur.execute(qry)
         else:
             self.cur.execute(qry, data)
                  
         

    def insert(self, qry="", data=[]):
         self.execute(qry, data)
         
    
    def query(self, qry):
        self.execute(qry, None)
        
    def fetchall(self):
        return self.cur.fetchall()
    
    def fetchone(self):
        return self.cur.fetchone()
    
    def record_exists(self, table="", column="", value=""):
        """format query"""
        qry = "SELECT id FROM %s WHERE %s = '%s'" % (table,column, value)
                        
        self.cur.execute(qry)
        
        # return the result
        return self.fetchone()
        
            
        
         


        
     
