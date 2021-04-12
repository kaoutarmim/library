from database import connection
import streamlit as st
import pandas as pd

def viewbooks(st, connection) :
    with connection.cursor() as cursor:
            choix = st.radio("choose an option : SHOW : ", ("ALL details", "authors" , "titles"))
            if choix == "ALL details":
                sql = 'SELECT * FROM books'
                cursor.execute(sql)
                result = cursor.fetchall() 
                df = pd.DataFrame(result)
                
            # options supplémentaires : 
            elif choix == "authors" :
                rq1 = 'SELECT DISTINCT author FROM books'
                cursor.execute(rq1)
                result = cursor.fetchall() 
                df = pd.DataFrame(result)
                
            elif choix == "titles" :
                rq2 = 'SELECT DISTINCT title FROM books'
                cursor.execute(rq2)
                result = cursor.fetchall() 
                df = pd.DataFrame(result)
    return st.table(df)

def viewFeedbacks(st,titleF):
    with connection.cursor() as cursor:
        query = 'SELECT * FROM infos where title ="{}"'.format(titleF)
        cursor.execute(query)
        result = cursor.fetchall() 
        if result :
            df = pd.DataFrame(result)
            return st.table(df)
        else:
            return st.warning('this title does not exist')

def AddBook(st,titleA,writer,ID,Email,description,Category):
    query1 = ("""INSERT INTO Books(title , Author, statut , déposé_par , emprunté_par, category) VALUES (%s, %s, %s, %s, %s, %s)""")
    query2 = ("""INSERT INTO Infos(title , Email, b_description , Rating) VALUES (%s, %s, %s, %s)""")
    with connection.cursor() as cursor:
        cursor.execute(query1,(titleA, writer, 'dispo' , ID , 'NULL' ,Category))
        cursor.execute(query2,(titleA, Email, description, 0))

        connection.commit() 
        st.success("Book added SUCCESSFULLY !")
       

def LendBook(st, titleC, ID):
    with connection.cursor() as cursor:
        query4 = 'SELECT COUNT(*) FROM books WHERE title = "{}" AND statut = "dispo"'.format(titleC)   
        cursor.execute(query4)
        result = cursor.fetchall()
        count=result[0]["COUNT(*)"]
        if  count==0:
            return st.warning("Error! Either the given title does not exist or the wanted book is not available now !")
        else :
            with connection.cursor() as cursor:
                UpdateStatut = ' UPDATE books SET statut = "non disponible" , emprunté_par="{}" WHERE title ="{}" '.format(ID,titleC)  
                cursor.execute(UpdateStatut)
                connection.commit()
            return  st.success("Book Lended SUCCESSFULLY !")
      

def RemoveBook(st, titleB,ID):
    with connection.cursor() as cursor:
        queryA='SELECT COUNT(*) from books where (`books`.`title`="{}" AND `books`.`déposé_par`="{}")'.format(titleB,ID)
        cursor.execute(queryA)
        result = cursor.fetchall()
        count=result[0]["COUNT(*)"]
        
        if  count==0:
            return st.warning("Either the given name does not exist Or the ID of the person who added this book doesn't match the given one, note that only the one who added something can delete it")
        else:
            with connection.cursor() as cursor:
                queryB ='DELETE FROM `books` WHERE `books`.`title`="{}" '.format(titleB)
                cursor.execute(queryB) 
                queryC='DELETE FROM `infos` WHERE `infos`.`title` ="{}" '.format(titleB)
                cursor.execute(queryC)  
                connection.commit()

            return st.success("Book removed SUCCESSFULLY !")


def ReturnBook(st,titleD,rating,ID):
    with connection.cursor() as cursor:
        query5 = 'SELECT COUNT(*) FROM books WHERE title ="{}" AND statut = "non disponible" AND emprunté_par="{}"'.format(titleD,ID)
        cursor.execute(query5) 
        result = cursor.fetchall()
        count=result[0]["COUNT(*)"]                                                                   
        if  count==0:
            return st.warning("ERROR ! Either the given title does not exist or the username of the one who lended the book does not match the given one !")
        else :
            with connection.cursor() as cursor:
                UpdateStatus = ' UPDATE books SET statut = "dispo" , emprunté_par="NULL" WHERE title = "{}"'.format(titleD)
                cursor.execute(UpdateStatus)
                connection.commit()
                query6= 'UPDATE infos SET rating={} WHERE title="{}"'.format(rating,titleD)
                cursor.execute(query6)
                connection.commit()
            return st.success("Book returned SUCCESSFULLY !")


#pour search 
c = connection.cursor()

def get_by_title(title):
    query = ('SELECT COUNT(*) FROM BOOKS WHERE title LIKE "%{}%" '.format(title))
    c.execute(query)
    result = c.fetchall()
    count=result[0]["COUNT(*)"]
        
    if  count==0 :
        return st.warning("ERROR !")
    else :
        st.info("titles of books !")
        c.execute('SELECT * FROM BOOKS WHERE title LIKE "%{}%" '.format(title))
        data = c.fetchall()
        df = pd.DataFrame(data)
        return st.table(df)


def get_by_author (author):
    query = ('SELECT COUNT(*) FROM BOOKS WHERE author LIKE "%{}%" '.format(author))
    c.execute(query)
    result = c.fetchall()
    count=result[0]["COUNT(*)"]
        
    if  count==0 :
        return st.warning("ERROR !")
    else :
        st.info("List of authors !")
        c.execute('SELECT * FROM BOOKS WHERE author LIKE "%{}%" '.format(author))
        data = c.fetchall()
        df = pd.DataFrame(data)
        return st.table(df)


def get_by_category (category):
    query = ('SELECT COUNT(*) FROM BOOKS WHERE category LIKE "%{}%" '.format(category))
    c.execute(query)
    result = c.fetchall()
    count=result[0]["COUNT(*)"]
        
    if  count==0 :
        return st.warning("ERROR !")
    else :
        st.info("List of categories !")
        c.execute('SELECT * FROM BOOKS WHERE category LIKE "%{}%" '.format(category))
        data = c.fetchall()
        df = pd.DataFrame(data)
        return st.table(df)