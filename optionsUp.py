from databaseUp import connection
import streamlit as st
import pandas as pd

def viewbooks(st, connection) :
     with connection.cursor() as cursor:
            sql = 'SELECT * FROM books'
            cursor.execute(sql)
            result = cursor.fetchall() 
            df = pd.DataFrame(result)
            st.table(df)


def ReturnBook(st, titleD):
    Booktitle = 'SELECT Title FROM books WHERE Title = "' +titleD+ '"'' AND statut = "non disponible" '
    with connection.cursor() as cursor:
        cursor.execute(Booktitle)
        try : 
            if cursor is None :
                st.warning("ERROR ! Can't find this book !")
            else :
                UpdateStatus = ' UPDATE books SET status = "dispo" WHERE Title ="' +titleD+ '"'
                cursor.execute(UpdateStatus)
                connection.commit()
                st.success("Book returned SUCCESSFULLY !")
        except : 
            st.warning("PLEASE Check the title of the book !")


    