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

ifconfig $INTERFACE:0 10.54.5.197
ifconfig $INTERFACE:1 10.54.5.193
ifconfig $INTERFACE:2 10.54.5.189
ifconfig $INTERFACE:3 10.54.5.185
ifconfig $INTERFACE:4 10.54.5.181
ifconfig $INTERFACE:5 10.54.5.177
ifconfig $INTERFACE:6 10.54.5.161
ifconfig $INTERFACE:7 10.54.5.2
ifconfig $INTERFACE:8 10.54.5.46
ifconfig $INTERFACE:9 10.54.17.1

route add -net 10.54.9.128 netmask 255.255.255.128 gw 10.54.5.45
route add -net 10.54.5.128 netmask 255.255.255.240 gw 10.54.5.45
route add -net 10.31.6.0 netmask 255.255.255.0 gw 10.54.5.45
route add -net 10.54.5.96 netmask 255.255.255.224 gw 10.54.5.45
route add -net 10.54.5.64 netmask 255.255.255.224 gw 10.54.5.45
route add -net 10.54.5.40 netmask 255.255.255.252 gw 10.54.5.45
route add -net 192.168.8.0 netmask 255.255.255.0 gw 10.54.5.45
route add -net 10.11.6.192 netmask 255.255.255.192 gw 10.54.5.45
