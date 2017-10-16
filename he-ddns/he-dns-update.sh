#!/bin/sh
while true
do
  curl -$type https://$hostname:$password@dyn.dns.he.net/nic/update?hostname=$hostname
  sleep 5m
done
