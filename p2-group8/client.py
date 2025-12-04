import socket
import os

# Make sure clientFiles folder exists
if not os.path.exists("clientFiles"):
    os.makedirs("clientFiles")

# Connect to server
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

    # -------------------- LS --------------------
    if cmd == 'ls':
        data = client.recv(4096).decode()
        print("Server files:\n" + data)

    # -------------------- GET --------------------
    elif cmd == 'get':
        if len(parts) < 2:
            print("Usage: get <filename>")
            continue

        filename = parts[1]
        status = client.recv(1024).decode()

        if status == 'OK':
            # Receive file data
            data = client.recv(4096)

            filepath = os.path.join("clientFiles", filename)
            with open(filepath, 'wb') as f:
                f.write(data)

            print(f"Downloaded '{filename}' successfully to clientFiles/")
        else:
            print(status)

    # -------------------- PUT --------------------
    elif cmd == 'put':
        if len(parts) < 2:
            print("Usage: put <filename>")
            continue

        filename = parts[1]
        filepath = os.path.join("clientFiles", filename)

        if not os.path.exists(filepath):
            print("File does not exist in clientFiles/")
            continue

        status = client.recv(1024).decode()

        if status == 'OK':
            with open(filepath, 'rb') as f:
                client.sendall(f.read())
            print(f"Uploaded '{filename}' successfully.")
        else:
            print(status)

    # -------------------- EXIT --------------------
    elif cmd == 'exit':
        response = client.recv(1024).decode()
        print(response)
        break

    # -------------------- UNKNOWN --------------------
    else:
        response = client.recv(1024).decode()
        print(response)

client.close()
print("Connection closed.")
