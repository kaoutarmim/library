import psycopg2

# Connect to the database
try :
    connection = psycopg2.connect(host='ec2-34-233-0-64.compute-1.amazonaws.com',
                                    port = '5432',
                                    user='vjbxphulrqayfn',
                                    password='89f51ae4dcf4cb65005199d2a7a0cbcfe0901fb853921a8a6b5cbf7eddba34c4',
                                    database='d9mp48vlj9fv9n')
except :
    print("Erreur lors de la connexion !")
