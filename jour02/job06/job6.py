import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    database='LaPlateforme'
)

cursor = cnx.cursor()

cursor.execute("SELECT SUM(capacite) AS total_capacite FROM salle")

resultat = cursor.fetchone()
print(f"La capacité de toutes les salles est de : {resultat[0]}")

cursor.close()
cnx.close()
