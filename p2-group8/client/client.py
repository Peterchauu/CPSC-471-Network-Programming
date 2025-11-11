import socket
import os

HOST = input("Enter server IP (or 'localhost'): ").strip()
PORT = 5000

client = socket.socket()
client.connect((HOST, PORT))
print(f"Connected to server at {HOST}:{PORT}")

while True:
    command = input("ftp> ").strip()
    if not command:
        continue

    client.send(command.encode())
    parts = command.split()
    cmd = parts[0]

    if cmd == 'ls':
        data = client.recv(4096).decode()
        print("Server files:\n" + data)

    elif cmd == 'get':
        if len(parts) < 2:
            print("Usage: get <filename>")
            continue
        filename = parts[1]
        status = client.recv(1024).decode()
        if status == 'OK':
            data = client.recv(4096)
            with open(filename, 'wb') as f:
                f.write(data)
            print(f"Downloaded '{filename}' successfully.")
        else:
            print(status)

    elif cmd == 'put':
        if len(parts) < 2:
            print("Usage: put <filename>")
            continue
        filename = parts[1]
        if not os.path.exists(filename):
            print("File does not exist on client side.")
            continue
        status = client.recv(1024).decode()
        if status == 'OK':
            with open(filename, 'rb') as f:
                client.sendall(f.read())
            print(f"Uploaded '{filename}' successfully.")
        else:
            print(status)

    elif cmd == 'quit':
        response = client.recv(1024).decode()
        print(response)
        break

    else:
        response = client.recv(1024).decode()
        print(response)

client.close()
print("Connection closed.")
