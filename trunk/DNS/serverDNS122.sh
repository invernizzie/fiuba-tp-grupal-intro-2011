#! /bin/bash

mkdir /etc/BackupBind
cp /etc/bind/* /etc/BackupBind/ -r --backup=numbered

mkdir /etc/bind/zones

echo "Copiando los archivos del server"
cp ./resto122/* /etc/bind/ -r

echo "Habilitamos el "
chmod 777 -R /etc/bind/

echo "Restarting BIND"
service bind9 restart

echo "Ejecucion finalizada"
