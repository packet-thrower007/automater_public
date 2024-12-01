#!/bin/bash

# Copyright 2023 Takuma Nakajima
# This software is released under the MIT license.
# https://opensource.org/license/mit/

# This shell script finds the maximum MTU size to the destination IP address by binary search.
#
# Example:
# $ ./find_max_mtu.sh 1.1.1.1
# checking MTU for 1500 bytes ... fail
# checking MTU for 800 bytes ... pass
# checking MTU for 1150 bytes ... pass
# checking MTU for 1325 bytes ... pass
# checking MTU for 1412 bytes ... fail
# checking MTU for 1368 bytes ... pass
# checking MTU for 1390 bytes ... pass
# checking MTU for 1401 bytes ... pass
# checking MTU for 1406 bytes ... pass
# checking MTU for 1409 bytes ... fail
# checking MTU for 1407 bytes ... fail
# checking MTU for 1406 bytes ... pass

# destination IP address must be specified in the first command line argument
if [ $# -ne 1 ]; then
  echo "usage: $0 <destination_ipaddress>"
  exit 1
fi

# use $dest for the destination IP address instead of $1
dest=$1

# set timeout in seconds for ICMP response
timeout=0.5

# set search range ($left, $right) for the size of MTU
# note: Since ICMP header (8 bytes) + IPv4 header (20 bytes) = 28 bytes,
#       the search range is 100-1500 bytes for left=72 and right=1472.
#       Please replace offset=28 to offset=48 for the IPv6 address.
#       (IPv6 header is 40 bytes)
offset=28
left=72
right=1472

# set initial state and start binary search
size=$right
prev=0

while true; do
  # check if the ICMP response is availble for $size + $offset (= MTU) bytes
  echo -n "checking MTU for $(expr $size + $offset) bytes ... "
  ping -c 1 -W $timeout -M do -s $size $dest >/dev/null 2>&1

  # update the search range
  if [ $? -eq 0 ]; then
    echo "pass"
    left=$size
  else
    echo "fail"
    right=$size
  fi

  # update $size for the new search range
  prev=$size
  size=$(expr $(expr $left + $right) / 2)

  # finish the process if the search range cannot be updated
  if [ $left -eq $right -o $size -eq $prev ]; then
    break
  fi
done
