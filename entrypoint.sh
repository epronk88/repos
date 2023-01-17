#!/bin/sh
service cron start 

#& tail -f /var/log/cron-1.log

sleep 5

/usr/local/bin/python3 /app/view.py