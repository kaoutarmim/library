import psycopg2

# Connect to the database
try :
    connection = psycopg2.connect(host='ec2-107-20-153-39.compute-1.amazonaws.com',
                                    port = '5432',
                                    user='hobdckukcaihdm',
                                    password='dcca3a52774599458a864d10455d93f2708437024cfd3e71e35dafd481afb5de',
                                    database='daac424rmim1m8')
except :
    print("Erreur lors de la connexion !")
