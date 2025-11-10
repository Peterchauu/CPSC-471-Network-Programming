import socket
import os

# Setup server
HOST = 'localhost'
PORT = 5000

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)
print(f"Server listening on {HOST}:{PORT}...")

conn, addr = server.accept()
print(f"Connected by {addr}")

while True:
    # Receive command from client
    data = conn.recv(1024).decode()
    if not data:
        break

    print(f"Client command: {data}")

    # Split the command
    parts = data.split()
    command = parts[0]

    # ----- LS COMMAND -----
    if command == 'ls':
        files = os.listdir('.')  # list all files in current directory
        file_list = '\n'.join(files)
        conn.send(file_list.encode())

    # ----- GET COMMAND -----
    elif command == 'get':
        if len(parts) < 2:
            conn.send(b'ERROR: No filename provided')
            continue
        filename = parts[1]
        if os.path.exists(filename):
            conn.send(b'OK')
            with open(filename, 'rb') as f:
                conn.sendall(f.read())
        else:
            conn.send(b'ERROR: File not found')

    # ----- PUT COMMAND -----
    elif command == 'put':
        if len(parts) < 2:
            conn.send(b'ERROR: No filename provided')
            continue
        filename = parts[1]
        conn.send(b'OK')
        with open(filename, 'wb') as f:
            data = conn.recv(1024)
            while data:
                f.write(data)
                if len(data) < 1024:
                    break
                data = conn.recv(1024)
        print(f"File {filename} received successfully")

    # ----- QUIT COMMAND -----
    elif command == 'quit':
        conn.send(b'Goodbye!')
        break

    else:
        conn.send(b'Unknown command')

conn.close()
server.close()
print("Server closed.")