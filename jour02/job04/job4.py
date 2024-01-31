import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    database='LaPlateforme'
)

cursor = cnx.cursor()

cursor.execute("SELECT nom, capacite FROM salle")

resultat = cursor.fetchall()
for row in resultat:
    print(row)

cursor.close()
cnx.close()
