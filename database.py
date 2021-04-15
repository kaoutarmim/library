'''import pymysql

# Connect to the database
try :
    connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='root',
                                    database='DATAcollection',
                                    cursorclass=pymysql.cursors.DictCursor)
except :
    print("Erreur lors de la connexion !")'''
    


import psycopg2

# Connect to the database
try :
    connection = psycopg2.connect(host='localhost',
                                    port = '5432',
                                    user='postgres',
                                    password='root',
                                    database='postgres')
except :
    print("Erreur lors de la connexion !")
cur = conn.cursor()
sql = '''CREATE TABLE person(
        ID INT PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        address TEXT NOT NULL
      ); '''
    
    cur.execute(sql)
    conn.commit()
sql = '''CREATE TABLE person(
        ID INT PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        address TEXT NOT NULL
      ); '''
    
    cur.execute(sql)
    conn.commit()
sql = '''CREATE TABLE person(
        ID INT PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        address TEXT NOT NULL
      ); '''
    
    cur.execute(sql)
    conn.commit()
