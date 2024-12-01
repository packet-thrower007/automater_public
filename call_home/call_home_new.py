import requests
import platform
import socket
import re
import uuid
import json
import psutil
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class SystemInfo:
    def __init__(self):
        self.public_ip = self.get_public_ip()
        self.platform = self.get_platform()
        self.platform_release = self.get_platform_release()
        self.platform_version = self.get_platform_version()
        self.architecture = self.get_architecture()
        self.hostname = self.get_hostname()
        self.ip_address = self.get_ip_address()
        self.mac_address = self.get_mac_address()
        self.processor = self.get_processor()
        self.ram = self.get_ram()

    # Getter Methods
    def get_public_ip(self):
        try:
            response = requests.get('https://ifconfig.me', timeout=5)
            response.raise_for_status()
            return response.text.strip()
        except requests.RequestException as e:
            logging.error(f"Failed to get public IP: {e}")
            return "Unavailable"

    def get_platform(self):
        return platform.system()

    def get_platform_release(self):
        return platform.release()

    def get_platform_version(self):
        return platform.version()

    def get_architecture(self):
        return platform.machine()

    def get_hostname(self):
        return socket.gethostname()

    def get_ip_address(self):
        try:
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            return ip
        except socket.error as e:
            logging.error(f"Failed to get IP address: {e}")
            return "Unavailable"

    def get_mac_address(self):
        try:
            mac_num = uuid.getnode()
            mac = ':'.join(re.findall('..', '%012x' % mac_num))
            return mac
        except Exception as e:
            logging.error(f"Failed to get MAC address: {e}")
            return "Unavailable"

    def get_processor(self):
        return platform.processor()

    def get_ram(self):
        try:
            ram_bytes = psutil.virtual_memory().total
            ram_gb = round(ram_bytes / (1024.0 ** 3), 2)
            return f"{ram_gb} GB"
        except Exception as e:
            logging.error(f"Failed to get RAM information: {e}")
            return "Unavailable"

    # Display Methods
    def show_public_ip(self):
        print(f"Public IP: {self.public_ip}")

    def show_platform(self):
        print(f"Platform: {self.platform}")

    def show_platform_release(self):
        print(f"Platform Release: {self.platform_release}")

    def show_platform_version(self):
        print(f"Platform Version: {self.platform_version}")

    def show_architecture(self):
        print(f"Architecture: {self.architecture}")

    def show_hostname(self):
        print(f"Hostname: {self.hostname}")

    def show_ip_address(self):
        print(f"IP Address: {self.ip_address}")

    def show_mac_address(self):
        print(f"MAC Address: {self.mac_address}")

    def show_processor(self):
        print(f"Processor: {self.processor}")

    def show_ram(self):
        print(f"RAM: {self.ram}")

    # Method to convert all info to a dictionary
    def to_dict(self):
        return {
            'public_ip': self.public_ip,
            'platform': self.platform,
            'platform_release': self.platform_release,
            'platform_version': self.platform_version,
            'architecture': self.architecture,
            'hostname': self.hostname,
            'ip_address': self.ip_address,
            'mac_address': self.mac_address,
            'processor': self.processor,
            'ram': self.ram
        }

    # Method to display all information
    def show_all_info(self):
        self.show_public_ip()
        self.show_platform()
        self.show_platform_release()
        self.show_platform_version()
        self.show_architecture()
        self.show_hostname()
        self.show_ip_address()
        self.show_mac_address()
        self.show_processor()
        self.show_ram()

if __name__ == "__main__":
    system_info = SystemInfo()

    # Option 1: Display all information using show methods
    # system_info.show_all_info()

    # Option 2: Print all information as a JSON string
    info_dict = system_info.to_dict()
    print(json.dumps(info_dict, indent=4))
