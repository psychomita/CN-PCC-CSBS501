import socket
import fcntl
import struct

def get_mac_address(interface):
    # Create a raw socket to perform low-level network operations
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Use ioctl to get the MAC address
    try:
        # Construct the ioctl request to get the hardware address
        mac = fcntl.ioctl(
            sock.fileno(),
            0x8927,  # SIOCGIFHWADDR: Get hardware address
            struct.pack('256s', interface[:15].encode('utf-8'))
        )[18:24]
        
        # Format and print the MAC address
        mac_address = ':'.join('%02X' % b for b in mac)
        return mac_address
    except OSError as e:
        print(f"Error: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    # Get the network interface from the user
    interface = input("Enter the network interface (e.g., eth0, wlan0): ")
    
    # Get and print the MAC address
    mac_address = get_mac_address(interface)
    if mac_address:
        print(f"MAC address of {interface}: {mac_address}")
