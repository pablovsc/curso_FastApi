import psycopg2

try:
    connection=psycopg2.connect(
        host = 'localhost',
        user = 'adempiere',
        password = 'adempiere'
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE mydatabase")
    print("hola")

except Exception as ex:
    print (ex)