mysql> SELECT id, nom, prenom, email, age
    -> FROM étudiant
    -> WHERE age BETWEEN 18 AND 25
    -> ORDER BY age ASC;
+----+-----------+----------+---------------------------------+-----+
| id | nom       | prenom   | email                           | age |
+----+-----------+----------+---------------------------------+-----+
|  3 | Doe       | John     | john.doe@laplateforme.io        |  18 |
|  6 | Dupuis    | Martin   | martin.dupuis@laplateforme.io   |  18 |
|  5 | Dupuis    | Gertrude | Gertrude.Dupuid@laplateforme.io |  20 |
|  1 | Spaghetti | Betty    | betty.Spaghetti@laplateforme.io |  23 |
+----+-----------+----------+---------------------------------+-----+
4 rows in set (0.01 sec)
