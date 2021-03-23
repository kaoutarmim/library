import streamlit as st
import numpy as np
import pandas as pd


st.title("JOKAS library")
st.subheader("READING IS TO THE MIND WHAT EXERCISE IS TO THE BODY")
st.subheader("This Space is made to share books between students, enjoy using it!")
st.sidebar.write("choose an option")


if st.sidebar.button(" View booklist"):
    df=pd.read_excel('C:\\Users\\SuperElectro\\Documents\\DATAcollection.xlsx',nrows=10)
    df 

         
#AddData(column):
#DeleteData(column):    
# Disponibility(title):
 
#L=["Add a book","Remove a book","Lend a book","Return a book","View book list"]
 

#Cases to fill in when adding a book 
 
if st.sidebar.button("Add a book"):
    title,writer=st.beta_columns(2)       
    title.text_input("Enter the title") 
    writer.text_input("Enter writer") 

    ID,phone=st.beta_columns(2)
    ID.text_input("Enter Student ID")
    phone.text_input("Enter phone number")

    Email=st.text_input('Enter Email')

    if st.button("submit"):
        st.success("You just added the book")

          

#Cases to fill in when deleting a book 
if st.sidebar.button("Remove a book") :
    titleB= st.text_input("Enter the title")
    WriterB= st.text_input("Enter the Writer")
    DeleteDate= st.text_input("Enter the removing date")
    st.button("submit")


if st.sidebar.button("Lend a book") :
    titleC= st.text_input("Enter the title of the wanted book")
    LendingDate= st.text_input("Enter today's date")
    StudentID= st.text_input("Enter your ID")
    st.button("submit")


if st.sidebar.button("Return a book") :
    titleD= st.text_input("Enter the title of the wanted book")
    ReturnDate= st.text_input("Enter today's date")
    StudentID= st.text_input("Enter your ID")
    st.button("submit")


if st.sidebar.button('SHOW STATISTICS'):
    st.write('later')   