import streamlit as st
st.title("JOKAS library")
st.subheader("READING IS TO THE MIND WHAT EXERCISE IS TO THE BODY")
st.subheader("This Space is made to share books between students, enjoy using it!")
st.sidebar.write("choose an option")

#FirstButtons

if st.sidebar.button('EXPLORE LIBRARY',key="A"):
     
#Adding options 
    choice=st.selectbox("You want to .. ?",["Add a book","Remove a book","Lend a book","Return a book","View book list"])
#Cases to fill in when adding a book 
    if choice=='Add a book':

        titleA= st.text_input("Enter the title","type here ...")
        WriterA= st.text_input("Enter the Writer","type here ...")
        AddDate= st.text_input("Enter the adding date","type here ...")
        #st.success("l'opération s'est bien effectué")
#Cases to fill in when deleting a book 
    if choice=='Remove a book' :
        titleB= st.text_input("Enter the title","type here ...")
        WriterB= st.text_input("Enter the Writer","type here ...")
        DeleteDate= st.text_input("Enter the removing date","type here ...")
     
#if st.button('View book list',key=3):


    if choice=='Lend a book' :
        titleC= st.text_input("Enter the title of the wanted book","type here ...")
        LendingDate= st.text_input("Enter today's date","type here ...")
        StudentID= st.text_input("Enter your ID","type here ...")
    
    if choice=='Return a book' :
        titleD= st.text_input("Enter the title of the wanted book","type here ...")
        ReturnDate= st.text_input("Enter today's date","type here ...")
        StudentID= st.text_input("Enter your ID","type here ...")
if st.sidebar.button('SHOW STATISTICS'):
    st.write('later')    