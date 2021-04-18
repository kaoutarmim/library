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
                df = df.rename(columns = {0: 'title', 1: 'author' , 2: 'statut' , 3:'déposé_par' , 4: 'emprunté_par' ,5 :'category' ,6:'lend_date' , 7: 'add_date'})
                
            # options supplémentaires : 
            elif choix == "authors" :
                rq1 = 'SELECT DISTINCT author FROM books'
                cursor.execute(rq1)
                result = cursor.fetchall() 
                df = pd.DataFrame(result)
                df = df.rename(columns = {0: 'author'})
                
            elif choix == "titles" :
                rq2 = 'SELECT DISTINCT title FROM books'
                cursor.execute(rq2)
                result = cursor.fetchall() 
                df = pd.DataFrame(result)
                df = df.rename(columns = {0: 'category'})
    return st.table(df)

def viewFeedbacks(st,titleF):
    with connection.cursor() as cursor:
        query = 'SELECT * FROM infos where title =%s'
        cursor.execute(query,(titleF,))
        result = cursor.fetchall() 
        if result :
            df = pd.DataFrame(result)
            df = df.rename(columns = {0: 'title', 1: 'email' , 2: 'b_Description' , 3:'rating'})
            return st.table(df)
        else:
            return st.warning('this title does not exist')


def upload(st,title,link):
        query = ("""INSERT INTO pdfs (title , uploaded_file) VALUES (%s, %s)""")
        with connection.cursor() as cursor:
            cursor.execute(query,(title,link))
            connection.commit() 
            st.success("Book added SUCCESSFULLY !")

def expload(st):
        query = ("SELECT title FROM pdfs")
        st.write("list of books")
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall() 
            df = pd.DataFrame(result)
            df = df.rename(columns = {0: 'title'})
            return st.table(df)

def generate_link(st,title):
    query = ("SELECT COUNT(*) FROM pdfs WHERE title=%s")
    with connection.cursor() as cursor:
        cursor.execute(query,(title,))
        result = cursor.fetchall()
        count=result[0][0]
        if  count== 0:
            return st.warning("Error! Please check the title of the book")
        else :
            with connection.cursor() as cursor:
                query = ("SELECT uploaded_file FROM pdfs WHERE title=%s")
                cursor.execute(query,(title,))
                result = cursor.fetchall()
                g_link=result[0][0]
                st.write("check this link to find you book: ")
                st.info(g_link)
        



def AddBook(st,titleA,writer,ID,Email,description,Category):
    query1 = ("""INSERT INTO Books(title , Author, statut , déposé_par , emprunté_par, category,add_date) VALUES (%s, %s, %s, %s, %s, %s,date(now()))""")
    query2 = ("""INSERT INTO Infos(title , Email, b_description , Rating) VALUES (%s, %s, %s, %s)""")
    with connection.cursor() as cursor:
        cursor.execute(query1,(titleA, writer, 'dispo' , ID , None ,Category))
        cursor.execute(query2,(titleA, Email, description, 0 ))

        connection.commit() 
        st.success("Book added SUCCESSFULLY !")
       

def LendBook(st, titleC, ID):
    with connection.cursor() as cursor:
        query4 = "SELECT COUNT(*) FROM books WHERE title=%s AND statut='dispo' " 
        cursor.execute(query4,(titleC,))
        result = cursor.fetchall()
        count=result[0][0]
        if  count== 0:
            return st.warning("Error! Either the given title does not exist or the wanted book is not available now !")
        else :
            with connection.cursor() as cursor:
                UpdateStatut = "UPDATE books SET statut ='non disponible' , emprunté_par=%s , lend_date= date(now()) WHERE title=%s "
                cursor.execute(UpdateStatut,(ID,titleC))
                connection.commit()
            return  st.success("Book Lended SUCCESSFULLY !")
      

def RemoveBook(st, titleB,ID):
    with connection.cursor() as cursor:
        queryA='SELECT COUNT(*) from books WHERE title=%s AND déposé_par=%s '
        cursor.execute(queryA,(titleB,ID))
        result = cursor.fetchall()
        count=result[0][0]
        
        if  count== 0:
            return st.warning("Either the given name does not exist Or the ID of the person who added this book doesn't match the given one, note that only the one who added something can delete it")
        else:
            with connection.cursor() as cursor:
                queryB ='DELETE FROM books WHERE title=%s '
                cursor.execute(queryB,(titleB,)) 
                queryC='DELETE FROM infos WHERE title=%s '
                cursor.execute(queryC,(titleB,))  
                connection.commit()

            return st.success("Book removed SUCCESSFULLY !")


def ReturnBook(st,titleD,rating,ID):
    with connection.cursor() as cursor:
        query5 = "SELECT COUNT(*) FROM books WHERE title=%s AND statut ='non disponible' AND emprunté_par=%s"
        cursor.execute(query5,(titleD,ID)) 
        result = cursor.fetchall()
        count=result[0][0]                                                                   
        if  count==0:
            return st.warning("ERROR ! Either the given title does not exist or the username of the one who lended the book does not match the given one !")
        else :
            with connection.cursor() as cursor:
                UpdateStatus = "UPDATE books SET statut='dispo' , lend_date=%s ,emprunté_par=%s WHERE title =%s"
                cursor.execute(UpdateStatus,(None, None ,titleD))
                connection.commit()
                query6= "UPDATE infos SET rating=%s WHERE title=%s"
                cursor.execute(query6,(rating,titleD))
                connection.commit()
            return st.success("Book returned SUCCESSFULLY !")


#pour search 
c = connection.cursor()

def get_by_title(title):
    query = ('SELECT COUNT(*) FROM BOOKS WHERE title=%s ')
    c.execute(query,(title,))
    result = c.fetchall()
    count=result[0][0]
        
    if  count==0 :
        return st.warning("ERROR !")
    else :
        st.info("titles of books !")
        query = ('SELECT * FROM BOOKS WHERE title=%s ')
        c.execute(query,(title,))
        data = c.fetchall()
        df = pd.DataFrame(data)
        return st.table(df)


def get_by_author (author):
    query = ('SELECT COUNT(*) FROM BOOKS WHERE author=%s ')
    c.execute(query,(author,))
    result = c.fetchall()
    count=result[0][0]
        
    if  count==0 :
        return st.warning("ERROR !")
    else :
        st.info("List of authors !")
        query = ('SELECT * FROM BOOKS WHERE author=%s ')
        c.execute(query,(author,))
        data = c.fetchall()
        df = pd.DataFrame(data)
        return st.table(df)


def get_by_category (category):
    query = ('SELECT COUNT(*) FROM BOOKS WHERE category=%s ')
    c.execute(query,(category,))
    result = c.fetchall()
    count=result[0][0]
        
    if  count==0 :
        return st.warning("ERROR !")
    else :
        st.info("List of categories !")
        query = ('SELECT * FROM BOOKS WHERE category=%s ')
        c.execute(query,(category,))
        data = c.fetchall()
        df = pd.DataFrame(data)
        return st.table(df)