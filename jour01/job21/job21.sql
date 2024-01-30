
mysql> SELECT COUNT(*)
    -> FROM étudiant
    -> WHERE age BETWEEN 18 AND 25;
+----------+
| COUNT(*) |
+----------+
|        3 |
+----------+
1 row in set (0.00 sec)
