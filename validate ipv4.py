import socket

def is_valid_ipv4(ip):
    try:
        socket.inet_pton(socket.AF_INET, ip)
        return True
    except socket.error:
        return False

# Test cases
ipv4_addresses = [
    "192.168.0.1",
    "10.0.0.255",
    "256.256.256.256",  # Invalid: Part > 255
    "192.168.1",        # Invalid: Missing parts
    "192.168.0.01"      # Invalid: Leading zeros
]

for ip in ipv4_addresses:
    if is_valid_ipv4(ip):
        print(f"{ip} is a valid IPv4 address.")
    else:
        print(f"{ip} is not a valid IPv4 address.")
