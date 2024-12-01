# Automater
Automater is a self contained archive that is designed to be portable, its purpose is to automate the day to day management of
Cisco and Palo Aloto Network devices.


## Supported Versions
1) Rocky Linux v9.4 Minimal
2) Rocky Linux v9.3 Minimal


## Installation

1) On your new AutomaterServer, complete the following:
   - cd /
   - dnf install git
   - git clone https://personal_access_token@github.com/packet-thrower007/automater.git

3) Execute the Setup Script:
   - cd /automater/
   - ./setup.sh


## Installation Complete

-----------------------------------------------------------------------------------------

## Configuration


                  Ping Monitor:    @ 15 Seconds Recurring      nano /automater/ping/ip_list.txt
                  Backups-IOS      @ 00:00:                    nano /automater/backup/backup_ios.csv
                  Backups-NXOS     @ 00:05:                    nano /automater/backup/backup_nxos.csv
                  Backups-SMB      @ 00:15:                    nano /automater/backup/backup_smb.csv
                  Zipper           @ 00:20:                    nano /automater/zipper/zipper.py
                  Uptime_Checker:  @ 02:00:                    nano /automater/uptime_checker/ios_devices.csv
                  Diff_Checker:    @ 03:00:                    nano /automater/diff_checker/diff_checker.py
                  backup_checker:  @ 05:00:                    nano /automater/backup_checker/backup_checker.py



## Configuration - Older Cisco Equipment
In the event you are unable to ssh into equipment due to ciphers etc, modify the following to enable legacy equipment.

1) Enable Legacy SSH
- nano /etc/ssh/ssh_config
- Uncomment the following line: Ciphers aes128-ctr,aes192-ctr,aes256-ctr,aes128-cbc,3des-cbc

2) Systemwide Crypto Policy
- update-crypto-policies --set LEGACY:NO-CBC
- nano /etc/crypto-policies/back-ends/openssh.config
-    Add the following to the line KexAlgorithms:  "diffie-hellman-group1-sha1"
-    Modify Keyside from 2048 to 1024: RequiredRSASize 1024
