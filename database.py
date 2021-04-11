import pymysql

# Connect to the database
try :
    connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='root',
                                    database='DATAcollection',
                                    cursorclass=pymysql.cursors.DictCursor)
except :
    print("Erreur lors de la connexion !")
