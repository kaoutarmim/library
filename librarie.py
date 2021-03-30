import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator


conn =sqlite3.connect('data.db')
c=conn.cursor()




#functions 
def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS table1(author TEXT,title TEXT,text TEXT ,date DATE)""") 
create_table()

def add_data(author,title,text,date):
    c.execute("""INSERT INTO table1(author,title,text,date) VALUES (?,?,?,?)""",(author,title,text,date))
    conn.commit()
def view_book():
    c.execute("""SELECT * FROM table1 """)
    data=c.fetchall()
    return data 
def view_titles():
    c.execute(""" SELECT DISTINCT title FROM table1""")
    data=c.fetchall()
    return data 

def get_blog_by_title(title):
    c.execute(""" SELECT * FROM table1 WHERE title="{}" """ .format(title))
    data=c.fetchall()
    return data 


def get_blog_by_author(author):
    c.execute(""" SELECT * FROM table1 WHERE author="{}" """ .format(author))
    data=c.fetchall()
    return data 

def delete_data(title):
    c.execute(""" DELETE FROM table1 WHERE title="{}" """.format(title))
    conn.commit()



title_temp = """
<div style = "background-color : #464e5f ;padding :10px,margin:10px;">
<h4 style="color:white;text -align : center;">{}</h4>
<h4 style="color:white;text -align : center;"> author:{}</h4>



<p>{}</p>


<h6 style="color:white;text -align : center;"> date:{}</h6>
</div>
"""






st.write("my library")
st.title("library")
Menu=["home","view books","add books","search","manage"]
choice=st.sidebar.selectbox("menu",Menu)

if choice=="home":
    st.subheader("home")
    r=view_book()
    st.write(r)
    for i in r:
        st.markdown(title_temp.format(i[0],i[1],i[2],i[3]),unsafe_allow_html=True)
    
    

if choice=="view books":
    st.subheader("view books")
    list_titles=[i[0] for i in view_titles() ]
    postlist=st.sidebar.selectbox("authors",list_titles)
    post_result= get_blog_by_title(postlist)
    for i in post_result:
        st.markdown(title_temp.format(i[0],i[1],i[2],i[3]),unsafe_allow_html=True)




if choice=="add books":
    st.subheader("add books")
    create_table()
    author=st.text_input("add the name of the book",max_chars=50)
    title=st.text_input("add the title of the author",max_chars=50)
    text=st.text_area("any thing to say about the book")
    date=st.date_input("date")
    if st.button("save"):
        add_data(author,title,text,date)
        st.success("book:{}saved".format(title))


if choice=="search":
    st.subheader("search books")
    search_term = st.text_input('enter search term')
    search_choice=st.radio("Field to search by",("title","author"))
    if st.button("search"):
        if search_choice == "title":
            article_result=get_blog_by_title(search_term)
        elif search_choice== "author":
            article_result= get_blog_by_author(search_term)


        for i in article_result:
            st.markdown(title_temp.format(i[1],i[0],i[2],i[3]),unsafe_allow_html=True)

    



if choice=="manage":
    st.subheader("manage")


    result=view_book()
    clean_db=pd.DataFrame(result,columns=["author","title","text","date"])
    st.dataframe(clean_db)


    unique_titles=[i[0] for i in view_titles() ]
    delete_blog_by_title=st.selectbox("unique titles",unique_titles)


    if st.button("Delete"):
        delete_data(delete_blog_by_title)
        st.warning("Delete: '{}'".format(delete_blog_by_title))

     

    if st.checkbox("metrics"):
        new_df= clean_db
        new_df['Length'] = new_df['text'].str.len()
        st.dataframe(new_df)




        st.subheader("author stats1")
        new_df["title"].value_counts().plot(kind='bar')
        st.pyplot()




        st.subheader("author stats2")
        new_df["title"].value_counts().plot.pie(autopct="%1.1f%%")
        st.pyplot()
    


    if st.checkbox("world cloud"):
        st.subheader("generate world cloud")
        #cloud= new_df['text'].iloc[0]
        cloud= ','.join(new_df['author'])
        WordCloud=WordCloud().generate(cloud)
        plt.imshow(WordCloud,interpolation='bilinear')
        plt.axis("off")
        st.pyplot()







    
  
