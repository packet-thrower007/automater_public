import os
from datetime import datetime
import time



while True:

    time.sleep(15)
    timestamp_long = datetime.now()
    current_time = timestamp_long.strftime("%D %H:%M:%S")

    with open("/automater/ping/ip_list.txt") as file:
        park = file.read()
        park = park.splitlines()
    for ip in park:
        response = os.popen(f"ping -c 2 {ip} ").read()
        # Pinging each IP address 2 times

        #saving some ping output details to output file
        if("100% packet loss" or "unreachable") in response:
            log = open("/automater/ping/log.txt", "a")
            log.write(current_time + " " + str(ip) + ' link is down'+'\n')
            log.close()
        else:
            pass
#            log = open("/automater/ping/log.txt","a")
#            log.write(current_time + " " + str(ip) + ' is up '+'\n')
#            log.close()

