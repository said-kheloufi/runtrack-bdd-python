mysql> SELECT id, nom, prenom, email, age
    -> FROM étudiant
    -> ORDER BY age ASC;
+----+-----------+----------+---------------------------------+-----+
| id | nom       | prenom   | email                           | age |
+----+-----------+----------+---------------------------------+-----+
|  4 | Barnes    | Binkie   | binkie.barnes@laplateforme.io   |  16 |
|  3 | Doe       | John     | john.doe@laplateforme.io        |  18 |
|  5 | Dupuis    | Gertrude | Gertrude.Dupuid@laplateforme.io |  20 |
|  1 | Spaghetti | Betty    | betty.Spaghetti@laplateforme.io |  23 |
|  2 | Chuck     | steak    | chuck.steak@laplateforme.io     |  45 |
+----+-----------+----------+---------------------------------+-----+
5 rows in set (0.00 sec)