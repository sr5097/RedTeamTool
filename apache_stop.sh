#!/bin/bash

while true
do
	sleep $((RANDOM % 10 + 1))
	sudo /usr/sbin/service apache2 stop
done
