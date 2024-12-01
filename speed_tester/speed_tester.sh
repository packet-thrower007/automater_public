#!/bin/bash

#Define the date & format it as a varable.
d=$(date +%Y-%m-%d:Time:%H:%M:%S)

#Run speedtest & append to file.
speedtest >> speed_test_log.txt

#Echo string & date appended into file.
echo "Tested on $d" >> speed_test_log.txt
