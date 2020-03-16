import pyodbc
import json
from configparser import ConfigParser



def serverConnection():
    parser = ConfigParser()
    parser.read('config.ini')

    username = parser.get('credentials', 'username')
    password = parser.get('credentials', 'password')
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL SERVER};'
                          'Server=USBLRRUCHIAGAR7\SQLEXPRESS;'
                          'Database=CDP_MONITOR;'
                          'Trusted_Connection=yes;'
                          )

    return conn

def getData(data):
    conn = serverConnection()
    cursor = conn.cursor()
    service = data["service"]
    rows = cursor.execute("[SRC_HIT] @SRV_NAME = '"+service+"'")
    data = []
    for row in rows.fetchall():
        data.append([x for x in row])
    print(data)
    return data


def insertData(data):
    conn = serverConnection()
    cursor = conn.cursor()
    print("Inserting Data: "+ json.dumps(data))
    print('Insert into [Pinning Table] (ID, [Service Name], Hit, [Source], [Seq No]) Values ('+data["ID"]+', \''+data["Service_Name"]+'\', '+data["Hit"]+', \''+data["Source"]+'\', '+data["Seq_No"]+')')
    cursor.execute('Insert into [Pinning Table] (ID, [Service Name], Hit, [Source], [Seq No]) Values ('+data["ID"]+', \''+data["Service_Name"]+'\', '+data["Hit"]+', \''+data["Source"]+'\', '+data["Seq_No"]+')')
    conn.commit()

def insertRequestData(data):
    conn = serverConnection()
    cursor = conn.cursor()
    print("Inserting Data: "+ json.dumps(data))
    print('Insert into [REQUEST_DATA] ([SERVICE],[REQUEST_TYPE],[REASON],[DESCRIPTION],[REQUESTOR_NAME],[CLIENT_NAME],[REQUESTOR_EMAIL],[SEND_COPY_TO]) Values (\'' + data["SERVICE"] + '\',\'' + data["REQUEST_TYPE"] + '\',\'' + data["REASON"] + '\', \'' + data["DESCRIPTION"] + '\', \'' + data["REQUESTOR_NAME"] + '\',\'' + data["CLIENT_NAME"] + '\',\'' + data["REQUESTOR_EMAIL"] + '\',\'' + data["SEND_COPY_TO"] + '\')')
    cursor.execute('Insert into [REQUEST_DATA] ([SERVICE],[REQUEST_TYPE],[REASON],[DESCRIPTION],[REQUESTOR_NAME],[CLIENT_NAME],[REQUESTOR_EMAIL],[SEND_COPY_TO]) Values (\'' + data["SERVICE"] + '\',\'' + data["REQUEST_TYPE"] + '\',\'' + data["REASON"] + '\', \'' + data["DESCRIPTION"] + '\', \'' + data["REQUESTOR_NAME"] + '\',\'' + data["CLIENT_NAME"] + '\',\'' + data["REQUESTOR_EMAIL"] + '\',\'' + data["SEND_COPY_TO"] + '\')')
    conn.commit()
    