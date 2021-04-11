import matplotlib 
from matplotlib import pyplot 
from options2 import *

from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
st.set_option('deprecation.showPyplotGlobalUse', False)

def statistics (st) :
        if st.checkbox("metrics"):
                st.subheader("Best BOOKs")
                with connection.cursor() as cursor:
                        sql = 'Select title , rating from infos order by rating DESC LIMIT 5'
                        cursor.execute(sql)
                        df = pd.DataFrame(cursor)
                        st.table(df)


                st.subheader("Author Stats")
                with connection.cursor() as cursor:
                        sql = 'SELECT author FROM books'
                        cursor.execute(sql)
                        df = pd.DataFrame(cursor)
                        df.value_counts().plot(kind = 'bar')
                        st.pyplot()

                
                st.subheader("stud Stats")
                with connection.cursor() as cursor:
                        sql = 'SELECT emprunté_par FROM books'
                        cursor.execute(sql)
                        df = pd.DataFrame(cursor)
                        df.value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
                        st.pyplot()

                st.subheader("CATEGORY Stats")
                with connection.cursor() as cursor:
                        sql = 'SELECT category FROM books'
                        cursor.execute(sql)
                        df = pd.DataFrame(cursor)
                        df.value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
                        st.pyplot()
                        
        
        if st.checkbox("world cloud"):

                title = st.text_input("enter a title")
                sql = 'SELECT b_description FROM infos WHERE title = "{}"'.format(title)
                with connection.cursor() as cursor:
                        cursor.execute(sql)
                        cloud = pd.DataFrame(cursor)
                        wcloud = cloud['b_description'].iloc[0]
                        #st.write(cloud)

                        if st.button("generate world cloud") :
                                Word_Cloud=WordCloud().generate(wcloud)
                                pyplot.imshow(Word_Cloud,interpolation='bilinear')
                                pyplot.axis("off")
                                st.pyplot()





