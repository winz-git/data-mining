#!/usr/bin/env python3

import sys

class db:
    conn = None
    
    host = "1"
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

    def commit(self):
        self.conn.commit()

    def close(self):
        #
        if (self.conn):
            self.conn.close()


    
