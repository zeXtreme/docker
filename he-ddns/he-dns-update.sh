#!/bin/sh
while true
do
  curl -$type -s -o ddns.log https://$hostname:$password@dyn.dns.he.net/nic/update?hostname=$hostname
  cat ddns.log
  sleep 1h
done
