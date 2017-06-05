
vagrant up 

sudo apt-get update
sudo apt-get install apache2 apache2-utils

 ### Protection d'un dossier
sudo htpasswd -c /etc/apache2/.htpasswd sammy

Ajouter dans /etc/apache2/sites-enabled/000-default.conf

```
<Directory "/var/www/html">
    AuthType Basic
    AuthName "Restricted Content"
    AuthUserFile /etc/apache2/.htpasswd
    Require valid-user
</Directory>
```

sudo service apache2 restart

---

## Fail2Ban

sudo apt-get install fail2ban

sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local

editer le fichier /etc/fail2ban/jail.local :

Enable apache auth ligne 208

sudo service fail2ban restart

Info sur les jails actives :
sudo fail2ban-client status

les régles de firewall iptables on été modifié en conséquence :
sudo iptables -S


Pour voir la jail apache en particulier :
sudo fail2ban-client status apache

Faire quelques essais d'authentification, l'IP sera bannie.

Voir règle REJECT iptables:
sudo iptables -L -v


Pour unban :
sudo fail2ban-client set apache unbanip 172.28.128.4

