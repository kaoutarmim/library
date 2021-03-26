import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             database='book',
                             cursorclass=pymysql.cursors.DictCursor)