import socket
HOST = '192.168.251.200'  # use the default IP address of the Raspberry Pi
PORT = 12345  # choose a free port number

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to a local address and port
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()
    print('Waiting for connection...')
    # Accept a connection
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            # Receive data from the client
            data = conn.recv(1024)
            if not data:
                break
            # Print the received data
            print('Received:', data.decode('utf-8'))
