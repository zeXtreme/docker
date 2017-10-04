#!/bin/sh
while true
do
  curl -$type -o ddns.log https://$hostname:$password@dyn.dns.he.net/nic/update?hostname=$hostname
  sleep 1h
done
