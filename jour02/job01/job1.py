import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="LaPlateforme",
)

cursor = cnx.cursor()

query = "SELECT * FROM étudiant"

cursor.execute(query)

for row in cursor:
    print(row)

cursor.close()
cnx.close()