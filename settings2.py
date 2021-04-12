from options2 import *
from stats import *
from Sign import *


def define(st):
    
    st.title("JOKAS Library")
    st.subheader("READING IS TO THE MIND WHAT EXERCISE IS TO THE BODY")
    st.write("This Space is made to share books between students, enjoy using it!")
  

def main(st):

    choice = st.sidebar.selectbox('Home',['Home','Discover lib','Sign Up','Sign In'])
    if choice =='Home' :
        st.image('NEW\lib.jpg', width = 600  )
        with st.beta_expander("NOTE !"):
            st.markdown("""
                In statisics section , we added an option to Create some awesome wordclouds 
                for your favourite books generated based on the description !
                """)
        st.subheader("About this app")
        st.markdown(""" This app is made to organize sharing books between students , you can create an account with an id to add,lend,remove,return a book ,
        and even without an account you can discover the library (different books,categories,authors) . """)
    if choice =='Sign Up' :
        st.info("Without An Account , you can Discover our Library !")
        SignUp(st)
    if choice =='Sign In'  :
        st.sidebar.subheader(" Welcome Back ! ")
        user = st.sidebar.text_input('Username')
        ID = st.sidebar.number_input(label = "Enter Student ID",step = 1, value = 0)
        passwd = st.sidebar.text_input('Password',type='password')
        if st.sidebar.checkbox("Login") :
            hashed_pswd = make_hashes(passwd)

            result = login_user(st,user,check_hashes(passwd,hashed_pswd),ID)
            if result:
                st.success("Logged In as {}".format(user))
                X=st.sidebar.selectbox('MENU',["Menu","View booklist","View Infos and Feedbacks", "Add Book","Remove a book","Lend a book","Return a book","Search Books",'SHOW STATISTICS'])
                options (st,X,ID)
            else :
                st.error("check your username or your ID or your password !")
        
    if choice =='Discover lib' :
        st.info("Without An Account , you can Discover our Library !")
        st.sidebar.write("choose an option")
        X=st.sidebar.selectbox('MENU',["Menu","View booklist","View Infos and Feedbacks","Search Books",'SHOW STATISTICS'])
        options (st,X,None)
   

def options (st,X,ID) :
    if X=="View booklist":
        viewbooks(st, connection)

    if X=="View Infos and Feedbacks":
        titleF=st.text_input('enter a title')
        viewFeedbacks(st,titleF)

    if X=="Add Book":
        titleA,writer =st.beta_columns(2)       
        titleA= st.text_input("Enter the title") 
        writer = st.text_input("Enter writer") 

        
        Category = st.text_input("enter category")
        Email = st.text_input("Enter your email")
        
        description=st.text_area("Give us a brief description of the book your are adding")
        if st.button("submit"):
            AddBook(st,titleA,writer,ID,Email,description,Category)   

    if X=="Remove a book":
        titleB= st.text_input("Enter the title")
        if st.button("submit"):
            RemoveBook(st, titleB,ID)

    if X=="Lend a book":
        titleC= st.text_input("Enter the title of the wanted book")
        if st.button("submit"):
            LendBook(st, titleC,ID)
 
    if X=="Return a book":
        titleD= st.text_input("Enter the title of the book")
        rating = st.number_input(label = "rate this book",step = 1, value = 0)
        if st.button("Submit"):
            ReturnBook(st, titleD,rating,ID)

    if X=='SHOW STATISTICS':
        statistics(st)

    if X=="Search Books":
        choice=st.radio("Search by",("category","author","title"))
        if choice=="category":
            categoryS=st.text_input("Enter A category")
            if st.button("Search"):
                get_by_category(categoryS)
        if choice=="author":
            authorS=st.text_input("Enter An author")
            if st.button("Search"):
                get_by_author (authorS)
        if choice=="title":
            titleS=st.text_input("Enter the title")
            if st.button("Search"):
                get_by_title (titleS)