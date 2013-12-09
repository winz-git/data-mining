import os,sys
lib_path = os.path.abspath('./scripts/library')
sys.path.append(lib_path)

import db_sqlite.dbSqlite as lite

print lite()


