#!/bin/bash

: '
The script sleeps for a random amount of time between 1 and 500 seconds
using the sleep command, and then stops the Apache service using the given
command. This loop will continue to run indefinitely until the script is 
interrupted or terminated.
'
while true		# Starts an infinite loop
do
	sleep $((RANDOM % 500 + 1))		# Sleep for a random amount of time (between 1 and 500 seconds)
	# Stop the Apache service using the sudo service command
	sudo /usr/sbin/service apache2 stop		
done
