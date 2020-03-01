import pyodbc
import json
from configparser import ConfigParser



def serverConnection():
    parser = ConfigParser()
    parser.read('config.ini')

    username = parser.get('credentials', 'username')
    password = parser.get('credentials', 'password')
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL SERVER};'
                          'Server=USHYDAPOOCH1\SQLEXPRESS;'
                          'Database=CDP_MONITOR;'
                          'UID='+username+';'
                          'PWD='+password+';'
                          'Trusted_Connection=yes;'
                          )

    return conn

def getData():
    conn = serverConnection()
    cursor = conn.cursor()
    rows = cursor.execute("[AGG_SRC_HIT]")
    data = []
    for row in rows.fetchall():
        data.append([x for x in row])
    return data

def insertData(data):
    conn = serverConnection()
    cursor = conn.cursor()
    print("Inserting Data: "+ json.dumps(data))
    print('Insert into [Pinning Table] (ID, [Service Name], Hit, [Source], [Seq No]) Values ('+data["ID"]+', \''+data["Service_Name"]+'\', '+data["Hit"]+', \''+data["Source"]+'\', '+data["Seq_No"]+')')
    cursor.execute('Insert into [Pinning Table] (ID, [Service Name], Hit, [Source], [Seq No]) Values ('+data["ID"]+', \''+data["Service_Name"]+'\', '+data["Hit"]+', \''+data["Source"]+'\', '+data["Seq_No"]+')')
    conn.commit()
