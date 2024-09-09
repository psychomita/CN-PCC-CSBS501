import socket
from datetime import datetime

# Server Configuration
host = '127.0.0.1'  # Localhost
port = 12345        # Arbitrary non-privileged port

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for incoming connections

    print(f"Server started at {host} on port {port}")
    print("Waiting for a connection...")

    while True:
        # Wait for a connection
        connection, client_address = server_socket.accept()

        with connection:
            print(f"Connected by {client_address}")

            # Get the current date and time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Send the current date and time to the client
            connection.sendall(current_time.encode())

            print(f"Sent to {client_address}: {current_time}")

