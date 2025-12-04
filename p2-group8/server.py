import socket
import os
import threading

HOST = '0.0.0.0'  # Accept connections from any IP
PORT = 5000

# Ensure server database directory exists
if not os.path.exists("serverDatabase"):
    os.makedirs("serverDatabase")

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

            # -------------------- LS --------------------
            if command == 'ls':
                files = os.listdir('serverDatabase')
                conn.send('\n'.join(files).encode())

            # -------------------- GET --------------------
            elif command == 'get':
                if len(parts) < 2:
                    conn.send(b'ERROR: No filename provided')
                    continue

                filename = parts[1]
                filepath = os.path.join('serverDatabase', filename)

                if os.path.exists(filepath):
                    conn.send(b'OK')
                    with open(filepath, 'rb') as f:
                        conn.sendall(f.read())
                    print(f"Sent file '{filename}' to {addr}")
                else:
                    conn.send(b'ERROR: File not found')

            # -------------------- PUT --------------------
            elif command == 'put':
                if len(parts) < 2:
                    conn.send(b'ERROR: No filename provided')
                    continue

                filename = parts[1]
                filepath = os.path.join('serverDatabase', filename)

                conn.send(b'OK')

                with open(filepath, 'wb') as f:
                    while True:
                        chunk = conn.recv(4096)
                        if not chunk:
                            break
                        f.write(chunk)
                        if len(chunk) < 4096:
                            break

                print(f"Received file '{filename}' from {addr}")

            # -------------------- EXIT --------------------
            elif command == 'exit':
                conn.send(b'Goodbye!')
                break

            # -------------------- UNKNOWN --------------------
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
    threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
