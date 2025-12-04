import socket
import os
import threading

HOST = '0.0.0.0'  # Accept connections from any IP
PORT = 5000

# Function to handle each client separately
def handle_client(conn, addr):
    print(f"New connection from {addr}")
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            parts = data.split()
            command = parts[0]

            if command == 'ls':
                files = os.listdir('.')
                conn.send('\n'.join(files).encode())

            elif command == 'get':
                if len(parts) < 2:
                    conn.send(b'ERROR: No filename provided')
                    continue
                filename = parts[1]
                if os.path.exists(filename):
                    conn.send(b'OK')
                    with open(filename, 'rb') as f:
                        conn.sendall(f.read())
                    print(f"Sent file '{filename}' to {addr}")
                else:
                    conn.send(b'ERROR: File not found')

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
                print(f"Received file '{filename}' from {addr}")

            elif command == 'exit':
                conn.send(b'Goodbye!')
                break

            else:
                conn.send(b'Unknown command')

        except:
            break

    conn.close()
    print(f"Connection closed: {addr}")

# Setup server
server = socket.socket()
server.bind((HOST, PORT))
server.listen(5)
print(f"Server listening on {HOST}:{PORT}")

while True:
    conn, addr = server.accept()
    # Start a new thread for each client
    threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
