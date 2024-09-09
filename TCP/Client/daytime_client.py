import socket

# Server Configuration
host = '127.0.0.1'  # The server's hostname or IP address
port = 12345        # The port used by the server

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connect to the server
    client_socket.connect((host, port))

    # Receive the data from the server
    data = client_socket.recv(1024)

    print("Received from server:", data.decode())

