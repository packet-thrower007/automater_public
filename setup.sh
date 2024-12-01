#!/usr/bin/env bash

echo "+++++++++++++++   Create Groups & Set Permissions                                  +++++++++++++++"
sleep 5
groupadd network_admin
chgrp -R network_admin /automater/*
chmod -R o=rwx,g=rwx,o-rwx /automater/*



echo "+++++++++++++++   Create User                                                       +++++++++++++++"
sleep 5
echo "Enter new username"
read username
useradd -m -s /bin/bash $username
passwd $username
usermod -d /automater/ $username


echo "+++++++++++++++   Adding "$username" to network_admin group                           +++++++++++++++"
sleep 5
usermod -a -G network_admin $username

echo "+++++++++++++++   Adding "$username" to wheel group   +++++++++++++++"
sleep 5
usermod -a -G wheel $username

echo "+++++++++++++++   Installing Required Software   +++++++++++++++"
sleep 5
dnf install -y epel-release >/dev/null
dnf install -y wget mlocate nano python git pip nmap telnet fail2ban figlet net-tools qemu-guest-agent whois >/dev/null
curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.rpm.sh | sudo bash >/dev/null
yum install speedtest
pip install netmiko >/dev/null 2>&1
pip install unzip >/dev/null 2>&1
pip install ping3 >/dev/null 2>&1
pip install time >/dev/null 2>&1
pip install colorama >/dev/null 2>&1
pip install termcolor >/dev/null 2>&1
pip install pyfiglet >/dev/null 2>&1


echo "+++++++++++++++   Update mlocatedb    +++++++++++++++"
sleep 5
updatedb >/dev/null



echo "+++++++++++++++   Creating Service Files   +++++++++++++++"
sleep 5
cp /automater/backup/automater_backup_ios.service /etc/systemd/system >/dev/null
cp /automater/backup/automater_backup_smb.service /etc/systemd/system >/dev/null
cp /automater/backup/automater_backup_nxos.service /etc/systemd/system >/dev/null
cp /automater/diff_checker/automater_diff_checker.service /etc/systemd/system >/dev/null
cp /automater/ping/automater_ping.service /etc/systemd/system >/dev/null
cp /automater/zipper/automater_zipper.service /etc/systemd/system >/dev/null
cp /automater/uptime_checker/automater_uptime_checker.service /etc/systemd/system >/dev/null
cp /automater/backup_checker/automater_backup_checker.service /etc/systemd/system >/dev/null


echo "+++++++++++++++   Reloading Systemd Daemon   +++++++++++++++"
sleep 5
systemctl daemon-reload >/dev/null


echo "+++++++++++++++   Enable Automater Services   +++++++++++++++"
sleep 5
systemctl enable automater_backup_ios.service >/dev/null
systemctl enable automater_backup_smb.service >/dev/null
systemctl enable automater_backup_nxos.service >/dev/null
systemctl enable automater_diff_checker.service >/dev/null
systemctl enable automater_ping.service >/dev/null
systemctl enable automater_zipper.service >/dev/null
systemctl enable automater_uptime_checker.service >/dev/null
systemctl enable automater_backup_checker.service >/dev/null
systemctl enable qemu-guest-agent >/dev/null

echo "+++++++++++++++   Starting Automater Services   +++++++++++++++"
sleep 5
systemctl start automater_backup_ios.service >/dev/null
systemctl start automater_backup_smb.service >/dev/null
systemctl start automater_backup_nxos.service >/dev/null
systemctl start automater_diff_checker.service >/dev/null
systemctl start automater_ping.service >/dev/null
systemctl start automater_zipper.service >/dev/null
systemctl start automater_uptime_checker.service >/dev/null
systemctl start automater_backup_checker.service >/dev/null
systemctl start qemu-guest-agent >/dev/null

echo "+++++++++++++++   Status of Automater Services   +++++++++++++++"
sleep 5
systemctl status automater_backup_ios.service >/dev/null 2>&1
systemctl status automater_backup_smb.service >/dev/null 2>&1
systemctl status automater_backup_nxos.service >/dev/null 2>&1
systemctl status automater_diff_checker.service >/dev/null 2>&1
systemctl status automater_ping.service >/dev/null 2>&1
systemctl status automater_zipper.service >/dev/null 2>&1
systemctl status automater_uptime_checker.service >/dev/null 2>&1
systemctl status automater_backup_checker.service >/dev/null 2>&1
systemctl status qemu-guest-agent >/dev/null 2>&1


echo "+++++++++++++++   Securing Ciphers Wizard   +++++++++++++++"
sleep 5
read -p "+++++++++++++++   Would you like to disable CBC Ciphers for SSH? [y/n]    ++++++++++++++" yn

case $yn in
   [Yy]* ) echo -e "cipher@tls = -AES-256-CBC -AES-128-CBC \ncipher = -AES-128-CBC -AES-256-CBC -CAMELLIA-256-CBC -CAMELLIA-128-CBC \ncipher@ssh = -AES-128-CBC -AES-256-CBC" > /etc/crypto-policies/policies/modules/NO-CBC.pmod;
           update-crypto-policies --set DEFAULT:NO-CBC
           systemctl restart sshd ;;
   [Nn]* ) exit;;
   * ) echo "Please answer y/n.";;
esac

echo "+++++++++++++++   Enabling keysize of 1024 for Older Devices    +++++++++++++++"
sleep 5
#unalias cp
/bin/cp -f /automater/configuration_files/openssh.config /etc/crypto-policies/back-ends/openssh.config >/dev/null 2>&1


echo "+++++++++++++++   Securing Server Services, Invalid SSH Logins will be blocked for 10 Minutes   +++++++++++++++"
sleep 5
cp /automater/configuration_files/jail.local /etc/fail2ban/jail.local >/dev/null 2>&1
systemctl enable fail2ban.service >/dev/null 2>&1
systemctl start fail2ban.service >/dev/null 2>&1
systemctl status fail2ban.service >/dev/null 2>&1


echo "+++++++++++++++   Creating Message of the Day Banner   +++++++++++++++"
sleep 5
cp /automater/configuration_files/motd.local /etc/motd


echo "+++++++++++++++   Harden Firewall   +++++++++++++++"
sleep 5
firewall-cmd --add-service "ntp" --permanent >/dev/null 2>&1
firewall-cmd --remove-service "cockpit" --permanent >/dev/null 2>&1
firewall-cmd --remove-service "dhcpv6-client" --permanent >/dev/null 2>&1
firewall-cmd --reload >/dev/null

echo "+++++++++++++++   Adding ASCI Art   +++++++++++++++"
date=$(date +%B" "%Y)
cp /automater/configuration_files/doom.flf /usr/share/figlet/ >/dev/null 2>&1
echo "figlet -c -f doom "Network Automater Appliance " ${date}" >> /etc/profile


echo "+++++++++++++++   Reloading Systemd Daemon   +++++++++++++++"
sleep 5
systemctl daemon-reload >/dev/null



echo "+++++++++++++++   NTP Server Coonfiguration Wizard   +++++++++++++++"
read -p "+++++++++++++++   Would you like to configure this as a NTP Server ? [y/n]" yn

case $yn in
   [Yy]* ) /bin/bash /automater/ntp_server/ntp_server.sh >/dev/null 2>&1;;
   [Nn]* ) exit;;
   * ) echo "Please answer y/n.";;
esac



echo "                  Setup Complete"
echo " "
echo " "
echo " "
echo "                  Ping Monitor:                          nano /automater/ping/ip_list.txt"
echo "                  Backups-IOS      @ 00:00:              nano /automater/backup/backup_ios.csv"
echo "                  Backups-SMB      @ 00:15:              nano /automater/backup/backup_smb.csv"
echo "                  Backups-NXOS     @ 00:05:              nano /automater/backup/backup_nxos.csv"
echo "                  Zipper           @ 00:20:              nano /automater/zipper/zipper.py"
echo "                  Uptime_Checker:  @ 00:30:              nano /automater/uptime_checker/ios_devices.csv"
echo "                  Diff_Checker:    @ 03:00:              nano /automater/diff_checker/diff_checker.py"
echo "                  backup_checker:  @ 04:00:              nano /automater/backup_checker/backup_checker.py"
