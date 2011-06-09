#! /bin/bash

# Utilizamos el primer parametro para especificar el paquete.
SERVICE=$1

SERVICE_INSTALL=$(dpkg --get-selections $SERVICE | sed "s/\t//g" | grep $SERVICE"install")

if [ -n "$SERVICE_INSTALL" ]; 
then 
    echo "$SERVICE service is already installed."; 
else
    echo "$SERVICE service is not installed.";
    apt-get install $SERVICE
fi

