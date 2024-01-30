mysql> SELECT id, nom, prenom, email, age
    -> FROM étudiant
    -> WHERE nom = 'Dupuis' AND prenom = 'Gertrude';
+----+--------+----------+---------------------------------+-----+
| id | nom    | prenom   | email                           | age |
+----+--------+----------+---------------------------------+-----+
|  5 | Dupuis | Gertrude | Gertrude.Dupuid@laplateforme.io |  20 |
+----+--------+----------+---------------------------------+-----+
1 row in set (0.04 sec)