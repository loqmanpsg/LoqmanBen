!/bin/bash

echo "Bienvenue dans le TP Github"
/etc/init.d/nginx status
/etc/init.d/nginx start
/etc/init.d/nginx status
ip a
ping 172.20.22.254 -c 5
