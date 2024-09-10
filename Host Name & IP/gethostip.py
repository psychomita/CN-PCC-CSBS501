import socket
import sys

def get_host_info(hostname):
    try:
        # Get the host information
        host_info = socket.gethostbyname_ex(hostname)
    except socket.gaierror:
        print("Error: No such host found")
        sys.exit(1)
    
    # The primary hostname
    print(f"Host name: {host_info[0]}")
    
    # All IP addresses associated with the host
    print("Host IP Addresses:")
    for ip in host_info[2]:
        print(ip)
    
    # Any aliases (other hostnames) for the host
    print("Other host names or aliases:")
    for alias in host_info[1]:
        print(alias)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gethostip.py nameofhost")
        sys.exit(1)
    
    hostname = sys.argv[1]
    get_host_info(hostname)
