import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="zoo"
    )

def add_animal(conn, animal):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO animal (name, race, cage_id, birth_date, origin_country)
        VALUES (%s, %s, %s, %s, %s)
    """, (animal['name'], animal['race'], animal['cage_id'], animal['birth_date'], animal['origin_country']))
    conn.commit()

def add_cage(conn, cage):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO cage (area, max_capacity)
        VALUES (%s, %s)
    """, (cage['area'], cage['max_capacity']))
    conn.commit()

def delete_animal(conn, animal_id):
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM animal WHERE id = %s
    """, (animal_id,))
    conn.commit()

def delete_cage(conn, cage_id):
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM cage WHERE id = %s
    """, (cage_id,))
    conn.commit()

def update_animal(conn, animal_id, animal):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE animal
        SET name = %s, race = %s, cage_id = %s, birth_date = %s, origin_country = %s
        WHERE id = %s
    """, (animal['name'], animal['race'], animal['cage_id'], animal['birth_date'], animal['origin_country'], animal_id))
    conn.commit()

def update_cage(conn, cage_id, cage):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE cage
        SET area = %s, max_capacity = %s
        WHERE id = %s
    """, (cage['area'], cage['max_capacity'], cage_id))
    conn.commit()

def list_animals(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM animal
    """)
    return cursor.fetchall()

def list_cages(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM cage
    """)
    return cursor.fetchall()

def total_cage_area(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT SUM(area) FROM cage
    """)
    return cursor.fetchone()[0]

def main():
    conn = connect_db()

    while True:
        print("1. Ajouter un animal")
        print("2. Ajouter une cage")
        print("3. Supprimer un animal")
        print("4. Supprimer une cage")
        print("5. Mettre à jour un animal")
        print("6. Mettre à jour une cage")
        print("7. Lister tous les animaux")
        print("8. Lister toutes les cages")
        print("9. Calculer la superficie totale des cages")
        print("10. Quitter")

        choice = int(input("Choisissez une option : "))

        if choice == 1:
            name = input("Entrez le nom de l'animal : ")
            race = input("Entrez la race de l'animal : ")
            cage_id = int(input("Entrez l'ID de la cage de l'animal : "))
            birth_date = input("Entrez la date de naissance de l'animal (YYYY-MM-DD) : ")
            origin_country = input("Entrez le pays d'origine de l'animal : ")
            animal = {'name': name, 'race': race, 'cage_id': cage_id, 'birth_date': birth_date, 'origin_country': origin_country}
            add_animal(conn, animal)
        elif choice == 2:
            area = float(input("Entrez la superficie de la cage : "))
            max_capacity = int(input("Entrez la capacité maximale de la cage : "))
            cage = {'area': area, 'max_capacity': max_capacity}
            add_cage(conn, cage)
        elif choice == 3:
            animal_id = int(input("Entrez l'ID de l'animal à supprimer : "))
            delete_animal(conn, animal_id)
        elif choice == 4:
            cage_id = int(input("Entrez l'ID de la cage à supprimer : "))
            delete_cage(conn, cage_id)
        elif choice == 5:
            animal_id = int(input("Entrez l'ID de l'animal à mettre à jour : "))
            name = input("Entrez le nouveau nom de l'animal : ")
            race = input("Entrez la nouvelle race de l'animal : ")
            cage_id = int(input("Entrez le nouvel ID de la cage de l'animal : "))
            birth_date = input("Entrez la nouvelle date de naissance de l'animal (YYYY-MM-DD) : ")
            origin_country = input("Entrez le nouveau pays d'origine de l'animal : ")
            animal = {'name': name, 'race': race, 'cage_id': cage_id, 'birth_date': birth_date, 'origin_country': origin_country}
            update_animal(conn, animal_id, animal)
        elif choice == 6:
            cage_id = int(input("Entrez l'ID de la cage à mettre à jour : "))
            area = float(input("Entrez la nouvelle superficie de la cage : "))
            max_capacity = int(input("Entrez la nouvelle capacité maximale de la cage : "))
            cage = {'area': area, 'max_capacity': max_capacity}
            update_cage(conn, cage_id, cage)
        elif choice == 7:
            animals = list_animals(conn)
            for animal in animals:
                print(animal)
        elif choice == 8:
            cages = list_cages(conn)
            for cage in cages:
                print(cage)
        elif choice == 9:
            total_area = total_cage_area(conn)
            print(f"La superficie totale de toutes les cages est de {total_area} m².")
        elif choice == 10:
            break
        else:
            print("Option non valide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
