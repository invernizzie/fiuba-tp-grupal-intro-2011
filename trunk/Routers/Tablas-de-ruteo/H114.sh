#! /bin/bash

echo "1" > /proc/sys/net/ipv4/ip_forward

INTERFACE=$(ifconfig -a | grep -o eth[0-9] | tail -n 1)

OTHER_INTS=$(ifconfig -a | grep -o eth[0-9]:[0-9])

for INT in $OTHER_INTS
do
ifconfig $INT down
done

#Borramos la tabla de routeo
ip route flush default

ifconfig $INTERFACE up

ifconfig $INTERFACE:0 10.54.5.45
ifconfig $INTERFACE:1 10.54.5.98
ifconfig $INTERFACE:2 10.54.9.132
ifconfig $INTERFACE:3 10.54.5.129

route add -net 10.54.5.184 netmask 255.255.255.252 gw 10.54.5.46
route add -net 10.54.5.180 netmask 255.255.255.252 gw 10.54.5.46
route add -net 10.11.6.192 netmask 255.255.255.192 gw 10.54.5.131
route add -net 10.54.5.0 netmask 255.255.255.224 gw 10.54.5.46
route add -net 10.54.5.40 netmask 255.255.255.252 gw 10.54.5.131
route add -net 10.54.5.188 netmask 255.255.255.252 gw 10.54.5.46
route add -net 10.54.5.196 netmask 255.255.255.252 gw 10.54.5.46
route add -net 10.54.5.64 netmask 255.255.255.224 gw 10.54.5.131
route add -net 10.31.6.0 netmask 255.255.255.0 gw 10.54.5.131
route add -net 10.54.5.176 netmask 255.255.255.252 gw 10.54.5.46
route add -net 192.168.8.0 netmask 255.255.255.0 gw 10.54.5.131
route add -net 10.54.5.160 netmask 255.255.255.252 gw 10.54.5.46
route add -net 10.54.17.0 netmask 255.255.255.0 gw 10.54.5.46
route add -net 10.54.5.192 netmask 255.255.255.252 gw 10.54.5.46
