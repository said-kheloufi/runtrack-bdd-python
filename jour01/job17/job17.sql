
mysql> SELECT id, nom, prenom, email, age
    -> FROM étudiant
    -> WHERE nom = 'Spaghetti';
+----+-----------+--------+---------------------------------+-----+
| id | nom       | prenom | email                           | age |
+----+-----------+--------+---------------------------------+-----+
|  1 | Spaghetti | Betty  | betty.Spaghetti@laplateforme.io |  20 |
+----+-----------+--------+---------------------------------+-----+
1 row in set (0.00 sec)
