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
                        sql = 'Select title , rating from infos order by rating DESC LIMIT 5'
                        cursor.execute(sql)
                        df = pd.DataFrame(cursor)
                        st.table(df)
                
                
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
                        You Create some awesome wordclouds 
                        for your favourite books generated based on the description !
                        """)

                title = st.text_input("enter a title")
                if st.button("generate world cloud") :
                        sql = 'SELECT b_description FROM infos WHERE title = "{}"'.format(title)
                        with connection.cursor() as cursor:
                                cursor.execute(sql)
                                cloud = pd.DataFrame(cursor)
                                st.write(cloud)
                                st.subheader("generating world cloud :") 
                                wcloud = cloud["b_description"].iloc[0]
                                

                                Word_Cloud=WordCloud(max_font_size=40).generate(wcloud)
                                pyplot.imshow(Word_Cloud,interpolation='bilinear')
                                pyplot.axis("off")
                                st.pyplot()





