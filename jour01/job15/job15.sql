mysql> SELECT id, nom, prenom, email, age
    -> FROM étudiant
    -> ORDER BY nom;
+----+-----------+----------+---------------------------------+-----+
| id | nom       | prenom   | email                           | age |
+----+-----------+----------+---------------------------------+-----+
|  4 | Barnes    | Binkie   | binkie.barnes@laplateforme.io   |  16 |
|  2 | Chuck     | steak    | chuck.steak@laplateforme.io     |  45 |
|  3 | Doe       | John     | john.doe@laplateforme.io        |  18 |
|  5 | Dupuis    | Gertrude | Gertrude.Dupuid@laplateforme.io |  20 |
|  6 | Dupuis    | Martin   | martin.dupuis@laplateforme.io   |  18 |
|  1 | Spaghetti | Betty    | betty.Spaghetti@laplateforme.io |  23 |
+----+-----------+----------+---------------------------------+-----+
6 rows in set (0.00 sec)
