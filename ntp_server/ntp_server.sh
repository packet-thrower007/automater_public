#!/usr/bin/env bash

echo "+++++++++++++++   Installing Chronyd   +++++++++++++++"
sleep 5

dnf install -y chrony >/dev/null

echo "+++++++++++++++   Import Configuration   +++++++++++++++"
sleep 5

cp /automater/configuration_files/chrony.local /etc/chrony.conf >/dev/null


echo "+++++++++++++++   Enable & Start Chronyd   +++++++++++++++"
sleep 5

systemctl enable chronyd >/dev/null
systemctl start chronyd >/dev/null
systemctl status chronyd >/dev/null

echo "+++++++++++++++   Chronyd Setup Complete   +++++++++++++++"
sleep 5
