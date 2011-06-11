#! /bin/bash

mkdir /etc/BackupBind
cp /etc/bind/* /etc/BackupBind/ --backup=numbered

mkdir /etc/bind/zones

echo "Copiando los archivos del server"
cp ./root116/* /etc/bind/ -r

echo "Habilitamos el "
chmod 777 -R /etc/bind/

echo "Restarting BIND"
service bind9 restart

echo "Ejecucion finalizada"
