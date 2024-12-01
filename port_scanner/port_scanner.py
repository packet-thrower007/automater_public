import socket
import sys
from datetime import datetime
import errno

target_hostname = input("What is the FQDN: ")
target_ip = socket.gethostbyname(target_hostname)

print("Enter the range of ports: ")

starting_port = input("Please enter the starting port: ")
ending_port = input("Please enter the last port: ")

time_init = datetime.now()

try:
	for port in range(int(starting_port),int(ending_port)):
		print("Scanning port {} ... ".format(port))
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(5)
		result = sock.connect_ex((target_ip, port))
		if result == 0:
			print("Port {}: Open".format(port))
		else:
			print("Port {}: Closed".format(port))
			print("Reason:",errno.errorcode[result])
		sock.close()
except KeyboardInterrupt:
	print("You pressed CTRL+C")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved. Exiting")
	sys.exit()
except socket.error:
	print("Couldn't connect to server")
	sys.exit()
time_finish = datetime.now()
total = time_finish - time_init

print("Port Scanning Completed in: ", total)


