import socket
import sys

def get_host_by_ip(ip_address):
    try:
        # Perform reverse DNS lookup to get host information
        host_info = socket.gethostbyaddr(ip_address)
    except socket.herror:
        print("Error: No such host found")
        sys.exit(1)
    
    # The primary hostname
    print(f"Host name: {host_info[0]}")

    # All IP addresses associated with the host (only one in most cases)
    print("Host IP Address:")
    print(ip_address)
    
    # Other addresses (aliases)
    print("Other addresses:")
    for alias in host_info[2]:
        print(alias)
    
    # Any aliases (other hostnames) for the host
    print("Other host names or aliases:")
    for alias in host_info[1]:
        print(alias)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gethostbyname.py ipaddress")
        sys.exit(1)
    
    ip_address = sys.argv[1]
    get_host_by_ip(ip_address)
