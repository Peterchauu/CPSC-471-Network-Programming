import socket
import os

# Server setup
HOST = 'localhost'
PORT = 5000

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)
print(f"Server listening on {HOST}:{PORT}...")

conn, addr = server.accept()
print(f"Connected by {addr}")

while True:
    # Receive command
    data = conn.recv(1024).decode()
    if not data:
        break

    print(f"Client command: {data}")
    parts = data.split()
    command = parts[0]

    # ----- LS COMMAND -----
    if command == 'ls':
        files = os.listdir()
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
            print(f"Sent file '{filename}' to client.")
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
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                f.write(data)
                if len(data) < 4096:
                    break
        print(f"Received file '{filename}' from client and saved to server's database")

    # ----- EXIT COMMAND -----
    elif command == 'exit':
        conn.send(b'Goodbye!')
        break

    else:
        conn.send(b'Unknown command')

conn.close()
server.close()
print("Server closed.")
