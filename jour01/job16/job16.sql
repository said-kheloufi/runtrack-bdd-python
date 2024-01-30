mysql> SELECT id, nom, prenom, email, age
    -> FROM étudiant
    -> WHERE prenom LIKE 'b%';
+----+-----------+--------+---------------------------------+-----+
| id | nom       | prenom | email                           | age |
+----+-----------+--------+---------------------------------+-----+
|  1 | Spaghetti | Betty  | betty.Spaghetti@laplateforme.io |  23 |
|  4 | Barnes    | Binkie | binkie.barnes@laplateforme.io   |  16 |
+----+-----------+--------+---------------------------------+-----+
2 rows in set (0.01 sec)