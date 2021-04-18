import matplotlib 
from matplotlib import pyplot 
from options2 import *

from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
st.set_option('deprecation.showPyplotGlobalUse', False)

def statistics (st) :
        if st.checkbox("statistics"):
                status = st.radio("Choose an option: ", ('authors', 'category'))

                if (status == 'authors'):
                        st.warning("stats of authors :")
                        with connection.cursor() as cursor:
                                sql = 'SELECT author FROM books'
                                cursor.execute(sql)
                                df = pd.DataFrame(cursor)
                                df.value_counts().plot(kind = 'bar')
                                st.pyplot()

                else:
                        st.warning("stats of categories :")
                        with connection.cursor() as cursor:
                                sql = 'SELECT category FROM books'
                                cursor.execute(sql)
                                df = pd.DataFrame(cursor)
                                df.value_counts().plot(kind = 'bar')
                                st.pyplot()

                st.subheader("Best BOOKs")
                with connection.cursor() as cursor:
                        sql = 'Select title , rating from infos WHERE rating is not %s order by rating DESC LIMIT 5'
                        cursor.execute(sql,(None,))
                        df = pd.DataFrame(cursor)
                        df = df.rename(columns = {0: 'title', 1: 'rating'})
                        st.table(df)

                st.subheader("Analyse")
                with connection.cursor() as cursor:
                        sql = "Select COUNT(*) from books WHERE statut='non disponible' AND lend_date=date(now()) "
                        cursor.execute(sql)
                        result = cursor.fetchall()
                        count=result[0][0]
                        st.write("number of books lended today :",count)

                        #analyse2
                        sql = "Select COUNT(*) from books WHERE add_date=date(now()) "
                        cursor.execute(sql)
                        result = cursor.fetchall()
                        count=result[0][0]
                        st.write("number of books added today :",count)
                        

                st.subheader("CATEGORY Stats")
                with connection.cursor() as cursor:
                        sql = 'SELECT category FROM books'
                        cursor.execute(sql)
                        df = pd.DataFrame(cursor)
                        df.value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
                        st.pyplot()
                
                
                st.subheader("stud Stats")
                with connection.cursor() as cursor:
                        sql = 'SELECT emprunté_par FROM books'
                        cursor.execute(sql)
                        df = pd.DataFrame(cursor)
                        df.value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
                        st.pyplot()
                        
        
        if st.checkbox("world cloud"):
                with st.beta_expander("NOTE !"):
                        st.markdown("""
                        You Can Create some awesome wordclouds 
                        for your favourite books generated based on the words entered related to the book title or based on the description !
                        """)

                title = st.text_input("enter a title")
                status = st.radio("Choose an option: ", ('enter some words related to the book title', 'based on the description'))
                st.subheader("generating world cloud :") 
                if (status == 'based on the description'):
                        sql = 'SELECT b_description FROM infos WHERE title = %s'
                        with connection.cursor() as cursor:
                                cursor.execute(sql,(title,))
                                cloud = pd.DataFrame(cursor)
                        
                        wcloud = cloud[0].iloc[0]
                        Word_Cloud=WordCloud(max_font_size=40, background_color="white").generate(wcloud)
                        pyplot.imshow(Word_Cloud,interpolation='bilinear')
                        pyplot.axis("off")
                        st.pyplot()
                else :
                        text = st.text_input("enter some words related to the book title")
                        if st.button("generate word cloud") :
                                wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
                                pyplot.imshow(wordcloud, interpolation="bilinear")
                                pyplot.axis("off")
                                st.pyplot()





