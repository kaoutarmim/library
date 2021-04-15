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
cur = connection.cursor()
sql = '''Create database DATAcollection; '''
    
cur.execute(sql)
connection.commit()
sql = '''CREATE TABLE books (
             title VARCHAR(100) NOT NULL PRIMARY KEY,
             author VARCHAR(40) NOT NULL,
             statut VARCHAR(20) NOT NULL,
             déposé_par SMALLINT NOT NULL,
             emprunté_par SMALLINT NOT NULL,
             category VARCHAR(50) ,
             lend_date datetime 
              
); '''
    
cur.execute(sql)
connection.commit()
sql = '''CREATE TABLE Infos(
             title VARCHAR(100) NOT NULL,
             Email VARCHAR(100) NOT NULL,
             b_Description TEXT,
             Rating SMALLINT,
             PRIMARY KEY(title)
)
; '''
    
cur.execute(sql)
connection.commit()
