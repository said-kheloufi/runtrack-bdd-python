mysql> SELECT id, nom, prenom, email, age
    -> FROM étudiant
    -> WHERE age = (SELECT MIN(age) FROM étudiant);
+----+--------+--------+-------------------------------+-----+
| id | nom    | prenom | email                         | age |
+----+--------+--------+-------------------------------+-----+
|  4 | Barnes | Binkie | binkie.barnes@laplateforme.io |  16 |
+----+--------+--------+-------------------------------+-----+
1 row in set (0.02 sec)
