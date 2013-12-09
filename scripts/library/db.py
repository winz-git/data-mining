import sys

class db:
    conn = None
    
    host = ""
    username = ""
    password = ""
    db = ""
    path = ""

    def __init__(self, host="", username="", password="", db="", path=""):
        #
        self.host = host
        self.username = username
        self.password = password
        self.db = db
        self.path = ""

    def connect(self):
        #

    def disconnect(self):
        #
        if (self.conn):
            self.conn.close()


    
