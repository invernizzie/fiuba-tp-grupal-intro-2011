#! /bin/bash

echo "Apago el Network Manager y otras yerbas"
chmod +x ./cleanNManagerAndOthers.sh
./cleanNManagerAndOthers.sh

echo "modifico el resolv.conf"
echo "domain resto.salta.dc.fi.uba.ar" > /etc/resolv.conf
echo "nameserver 10.54.5.46" >> /etc/resolv.conf

