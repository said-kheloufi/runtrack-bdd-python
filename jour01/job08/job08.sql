mysql> SELECT id, nom, prenom, email, age
    -> FROM étudiant
    -> WHERE age < 18;
+----+--------+--------+-------------------------------+-----+
| id | nom    | prenom | email                         | age |
+----+--------+--------+-------------------------------+-----+
|  4 | Barnes | Binkie | binkie.barnes@laplateforme.io |  16 |
+----+--------+--------+-------------------------------+-----+
1 row in set (0.00 sec)