import pyodbc
CN='DRIVER=ODBC Driver 17 for SQL Server;SERVER=tcp:purenweb.database.windows.net;PORT=1433;DATABASE=purenweb;UID=purenweb;PWD=Zvi30600'
connDB = pyodbc.connect(CN)
cursorDB = connDB.cursor()

def conDB():
    conDB = pyodbc.connect(CN)
    cursorDB = conDB.cursor()

def PubExecute(sSql):
    conDB()
    cursorDB.execute(sSql)
    connDB.commit()

def PubExecuteScalar(sSql):
    conDB()
    cursorDB.execute(sSql)
    return cursorDB.fetchall()


