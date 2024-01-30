mysql> SELECT id, nom, prenom, email, age
    -> FROM étudiant
    -> ORDER BY age DESC;
+----+-----------+----------+---------------------------------+-----+
| id | nom       | prenom   | email                           | age |
+----+-----------+----------+---------------------------------+-----+
|  2 | Chuck     | steak    | chuck.steak@laplateforme.io     |  45 |
|  1 | Spaghetti | Betty    | betty.Spaghetti@laplateforme.io |  23 |
|  5 | Dupuis    | Gertrude | Gertrude.Dupuid@laplateforme.io |  20 |
|  3 | Doe       | John     | john.doe@laplateforme.io        |  18 |
|  4 | Barnes    | Binkie   | binkie.barnes@laplateforme.io   |  16 |
+----+-----------+----------+---------------------------------+-----+
5 rows in set (0.00 sec)