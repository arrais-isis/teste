import mysql.connector

banco = mysql.connector.connect(
    host="10.30.29.162",
    port=3309,
    user="root",
    password="root123",
    database="isis"
)

cursor = banco.cursor()

# cursor.execute("CREATE TABLE teste (ID INT PRIMARY KEY, NOME TEXT);")
cursor.execute("INSERT INTO teste VALUES (1, 'vinicius')")
banco.commit() # Usado em caso de alteração nos dados (insert, delete, update)

