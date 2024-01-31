import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    database='LaPlateforme'
)

cursor = cnx.cursor()

cursor.execute("SELECT SUM(superficie) AS total_superficie FROM etage")

resultat = cursor.fetchone()
print(f"La superficie de La Plateforme est de {resultat[0]} m2")

cursor.close()
cnx.close()
