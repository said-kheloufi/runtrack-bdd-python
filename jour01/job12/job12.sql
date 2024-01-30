mysql> INSERT INTO étudiant (nom, prenom, email, age)
    -> VALUES ('Dupuis', 'Martin', 'martin.dupuis@laplateforme.io', 18);
                                                                       
Query OK, 1 row affected (0.03 sec)

mysql> SELECT * FROM étudiant WHERE nom = 'Dupuis';
+----+--------+----------+-----+---------------------------------+
| id | nom    | prenom   | age | email                           |
+----+--------+----------+-----+---------------------------------+
|  5 | Dupuis | Gertrude |  20 | Gertrude.Dupuid@laplateforme.io |
|  6 | Dupuis | Martin   |  18 | martin.dupuis@laplateforme.io   |
+----+--------+----------+-----+---------------------------------+
2 rows in set (0.01 sec)