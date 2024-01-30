mysql> SELECT id, nom, prenom, email, age
    -> FROM étudiant
    -> WHERE age = (SELECT MAX(age) FROM étudiant);
+----+-------+--------+-----------------------------+-----+
| id | nom   | prenom | email                       | age |
+----+-------+--------+-----------------------------+-----+
|  2 | Chuck | steak  | chuck.steak@laplateforme.io |  45 |
+----+-------+--------+-----------------------------+-----+
1 row in set (0.00 sec)