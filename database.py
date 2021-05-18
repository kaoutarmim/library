import psycopg2

# Connect to the database
try :
    connection = psycopg2.connect(host='ec2-54-243-92-68.compute-1.amazonaws.com',
                                    port = '5432',
                                    user='hchiffxlaljevd',
                                    password='4742d537454bc7f4bd67c05125d5689564129bc6129039ff0a22c6bbb5aec66c',
                                    database='dbql1dl1uspdmg')
except :
    print("Erreur lors de la connexion !")
