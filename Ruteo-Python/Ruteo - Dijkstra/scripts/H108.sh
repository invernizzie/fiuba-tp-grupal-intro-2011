#! /bin/bash

echo "1" > /proc/sys/net/ipv4/ip_forward

INTERFACE=$(ifconfig -a | grep -o eth[0-9] | tail -n 1)

OTHER_INTS=$(ifconfig -a | grep -o eth[0-9]:[0-9])

for INT in $OTHER_INTS
do
ifconfig $INT down
done

ifconfig $INTERFACE up

ifconfig $INTERFACE:0 10.54.5.41
ifconfig $INTERFACE:1 10.54.5.68

route add -net 10.54.9.128 netmask 255.255.255.128 gw 10.54.5.42
route add -net 10.54.5.180 netmask 255.255.255.252 gw 10.54.5.42
route add -net 10.11.6.192 netmask 255.255.255.192 gw 10.54.5.66
route add -net 10.54.5.0 netmask 255.255.255.224 gw 10.54.5.42
route add -net 10.31.6.0 netmask 255.255.255.0 gw 10.54.5.66
route add -net 10.54.5.128 netmask 255.255.255.240 gw 10.54.5.42
route add -net 10.54.5.188 netmask 255.255.255.252 gw 10.54.5.42
route add -net 10.54.5.96 netmask 255.255.255.224 gw 10.54.5.42
route add -net 10.54.5.196 netmask 255.255.255.252 gw 10.54.5.42
route add -net 10.54.5.184 netmask 255.255.255.252 gw 10.54.5.42
route add -net 10.54.5.176 netmask 255.255.255.252 gw 10.54.5.42
route add -net 192.168.8.0 netmask 255.255.255.0 gw 10.54.5.66
route add -net 10.54.5.44 netmask 255.255.255.252 gw 10.54.5.42
route add -net 10.54.17.0 netmask 255.255.255.0 gw 10.54.5.42
route add -net 10.54.5.160 netmask 255.255.255.252 gw 10.54.5.42
route add -net 10.54.5.192 netmask 255.255.255.252 gw 10.54.5.42
