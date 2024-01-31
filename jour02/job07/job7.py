import mysql.connector

class Salarie:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = self.cnx.cursor()

    def create(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.cnx.commit()

    def read(self):
        query = "SELECT * FROM employe"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update(self, id, nom, prenom, salaire, id_service):
        query = "UPDATE employe SET nom = %s, prenom = %s, salaire = %s, id_service = %s WHERE id = %s"
        values = (nom, prenom, salaire, id_service, id)
        self.cursor.execute(query, values)
        self.cnx.commit()

    def delete(self, id):
        query = "DELETE FROM employe WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        self.cnx.commit()

cnx = mysql.connector.connect(
    user='root', 
    password='root', 
    host='localhost', 
    database='Entreprise')
salarie = Salarie(cnx)

salarie.create('Dupont', 'Jean', 3500.00, 1)

employes = salarie.read()
for employe in employes:
    print(employe)

salarie.update(1, 'Dupont', 'Jean-Pierre', 4000.00, 1)

salarie.delete(1)

cnx.close()
