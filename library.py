import streamlit as st
import numpy as np
import pandas as pd


st.title("JOKAS library")
st.subheader("READING IS TO THE MIND WHAT EXERCISE IS TO THE BODY")
st.subheader("This Space is made to share books between students, enjoy using it!")
st.sidebar.write("choose an option")


         
 
#AvailableOptions=["Add a book","Remove a book","Lend a book","Return a book","View book list"]

#View book list
if st.sidebar.button(" View booklist"):
    df=pd.read_excel('C:\\Users\\SuperElectro\\Documents\\DATAcollection.xlsx',nrows=10)
    df 

#Cases to fill in when adding a book 
if st.sidebar.button("Add a book"):
    st.header('Adding Form')
    title,writer=st.beta_columns(2)       
    title.text_input("Enter the title") 
    writer.text_input("Enter writer") 
    AddDate= st.date_input("Enter today's date")
    ID,Email=st.beta_columns(2)
    ID.text_input("Enter your Student ID")
    Email.text_input("Enter Email")
    
    if st.button("submit"):
#Adding the book to dataframa
        df=df.append({'book name' : title , 'author' : writer, 'STATUT (dispo ou pas )' : 'dispo','déposé par (ID)' : ID,'emprunté par' : 'null'} , ignore_index=True)
        st.success("Thank you for adding this book to Jokas library ")

          

#Cases to fill in when deleting a book 
if st.sidebar.button("Remove a book") :
    st.header('Deleting Form')
    titleB= st.text_input("Enter the title")
    WriterB= st.text_input("Enter the Writer")
    IDD=st.text_input(" Enter your ID")
    if st.button("submit"):
#Condition to delete a book
        if df['déposé par (ID)'] == IDD:
            indexNames = df[ df['book name'] == titleB ].index 
            df.drop(indexNames , inplace=True)
            st.success("You just deleted the book")
        else:
            st.warning("The ID of the person who added this book doesn't match the given one, note that only the one who added it can delete it")

#Cases to fill in when Lending a book 
if st.sidebar.button("Lend a book") :
    st.header('Lending Form')
    titleC= st.text_input("Enter the title of the wanted book")
    StudentID= st.text_input("Enter your ID")
    UserName=st.text_input("Enter your userName")
    if st.button("submit"):
        for i in df.index:
#loop to find the book and then condition to success the lending processus
            if df['book name'] == titleC:
                if df['STATUT (dispo ou pas )'] == 'dispo':
                    df['STATUT (dispo ou pas )'] ='Non dispo'
                    st.success("The wanted book is available now, you pass by the library's office to take it")
                else:
                    st.warning("Sorry, the wanted book is not available now")
            else:
                i+=1
        

#Cases to fill in when Returning a book 
if st.sidebar.button("Return a book") :
    st.header('Returning Form')
    titleD= st.text_input("Enter the title of the wanted book")
    StudentID= st.text_input("Enter your ID")
    UserNamee=st.text_input("Enter your userName")
    if st.button("submit"):
#loop to find the book 
        for i in df.index:
            if df['book name'] == titleD:
#Changing the book's Status to become Available
                df['STATUT (dispo ou pas )'] = 'dispo'
                st.write('thanks for returning the book, hope you enjoyed reading it!')
            else:
                i+=1
        



if st.sidebar.button('SHOW STATISTICS'):
    st.write('later')   