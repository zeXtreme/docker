#!/bin/sh
while true
do
  curl -$type https://$hostname:$password@dyn.dns.he.net/nic/update?hostname=$hostname >> ddns.log
  sleep 1h
done
