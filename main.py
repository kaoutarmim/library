from database import connection
from settings2 import *

cur = conn.cursor()
sql = '''Create database DATAcollection; '''
    
    cur.execute(sql)
    conn.commit()
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
    conn.commit()
sql = '''CREATE TABLE Infos(
             title VARCHAR(100) NOT NULL,
             Email VARCHAR(100) NOT NULL,
             b_Description TEXT,
             Rating SMALLINT,
             PRIMARY KEY(title)
)
; '''
    
    cur.execute(sql)
    conn.commit()

define(st)


if __name__ == '__main__':
    main(st)
