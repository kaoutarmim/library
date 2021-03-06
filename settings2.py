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
        st.image('https://elearningindustry.com/wp-content/uploads/2020/05/social-learning-examples-for-your-online-library.jpg', width = 600  )
        with st.beta_expander("NOTE !"):
            st.markdown("""
                In statisics section , we added an option to Create some awesome wordclouds 
                for your favourite books !
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
                X=st.sidebar.selectbox('MENU',["Menu","View booklist","View Infos and Feedbacks", "pdf Books", "Add Book","Remove a book","Lend a book","Return a book","Search Books","SHOW STATISTICS","contribute","Student propositions"])
                options (st,X,ID)
            else :
                st.error("check your username or your ID or your password !")
        
    if choice =='Discover lib' :
        st.info("Without An Account , you can Discover our Library !")
        st.sidebar.write("choose an option")
        X=st.sidebar.selectbox('MENU',["Menu","View booklist","View Infos and Feedbacks","Search Books","SHOW STATISTICS","contribute","Student propositions"])
        options (st,X,None)
   

def options (st,X,ID) :
    if X=="View booklist":
        viewbooks(st, connection)

    if X=="View Infos and Feedbacks":
        titleF=st.text_input('enter a title')
        viewFeedbacks(st,titleF)

    if X=="pdf Books":
        
        status = st.radio("Choose an option: ", ('upload', 'download'))

        if (status=='upload') :
            title = st.text_input("enter a title")
            link = st.text_input("enter the link ")

            if st.button("submit") :
                upload(st,title,link)
        
        else :
            ch = st.radio("Choose an option: ", ('view booklist', 'search for a link'))
            if ch == 'view booklist':
                expload(st)
            else : 
                title = st.text_input("enter a title")
                if st.button("get the link") :
                    generate_link(st,title)

            

        

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
            LendBook(st,titleC,ID)
 
    if X=="Return a book":
        titleD= st.text_input("Enter the title of the book")
        rating = st.number_input(label = "rate this book",step = 1, value = 0)
        if st.button("Submit"):
            ReturnBook(st, titleD,rating,ID)

    if X=="SHOW STATISTICS":
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


    if X=="contribute":
        titleB= st.text_input("Enter your favourite category")
        titleC= st.text_input("Enter a book you wanna see next time ")
        if st.button("submit"):
            query1 = ("""INSERT INTO contribute (favourite_category,books_propositions) VALUES (%s, %s)""")
            with connection.cursor() as cursor:
                cursor.execute(query1,(titleB, titleC))

                connection.commit() 
                st.success("Your Proposition is taken into account !")
            
            
    if X=="Student propositions":
        with connection.cursor() as cursor:
            if st.checkbox("book needs"):
                query = 'SELECT books_propositions FROM contribute'
                cursor.execute(query)
                result = cursor.fetchall() 
                df = pd.DataFrame(result)
                st.table(df)
            
            if st.checkbox("needs categories"):
                st.write('most needed categories are:')
                query = 'SELECT DISTINCT favourite_category FROM contribute'
                cursor.execute(query)
                result = cursor.fetchall() 
                df = pd.DataFrame(result)
                st.table(df)

             
            
    