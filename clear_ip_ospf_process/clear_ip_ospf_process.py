#!/usr/bin/env python3

from netmiko import ConnectHandler

device = {
    "host": "8.8.8.8",
    "device_type": "cisco_xe",
    "username": "cisco",
    "password": "cisco123",
    "secret": "",  # Enable password (If applicable)
}

# Connect to the device
conn = ConnectHandler(**device)

# Check if connected in user mode and enter enable mode
# Make sure you have the "secret": "xxxx" is set in device var
if not conn.check_enable_mode():
    conn.enable()

# Notice send_command_timing method here
clear_process = conn.send_command_timing("clear ip ospf process")
provide_answer = conn.send_command_timing("yes")

# Disconnect to clear the vty line
conn.disconnect()
