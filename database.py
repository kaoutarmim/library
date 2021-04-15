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
