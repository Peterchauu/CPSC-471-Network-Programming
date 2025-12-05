Project: Client-to-Server File Transfer using Sockets

-------------------------------------------

Collaborators:

Bryan Tran | Email: btran299@csu.fullerton.edu
Peter Chau | Email: Peterchauu93@csu.fullerton.edu

Language: Python 3

-------------------------------------------

Description:
This project implements a multi-client file transfer protocol (FTP) system using Python sockets and threading.
It allows multiple clients to connect to the server concurrently and perform basic FTP-like operations:

- ls   : list files on the server
- get  : download a file from the server
- put  : upload a file to the server
- exit : disconnect from the server

The server uses threads to handle multiple clients simultaneously. Clients can connect from local machines or, later, from other hosts including an AWS EC2 instance.

-------------------------------------------

How to Run (Local Testing):

1. Place `server.py`, `client.py`, and any test files in one folder named:
   p2-group8

2. Open one terminal and start the server:
   python3 server.py

3. Open one or more terminals to start clients:
   python3 client.py

4. When prompted, enter the server IP:
   - For local testing, use `localhost`
   - For EC2 testing, use the public IP of your server instance

5. Type commands in the client terminal:
   ftp> ls
   ftp> get test1.txt
   ftp> put test2.txt
   ftp> exit

-------------------------------------------

Notes:
- The server must be started before clients connect.
- Multiple clients can connect at the same time and transfer files independently.
- Test files (like `test1.txt` and `test2.txt`) can be added to the folder for GET/PUT commands.
- Server listens on port 5000.
- Make sure Python 3 is installed on all machines used for testing.
- Local testing was done using WSL2 Ubuntu terminal.

-------------------------------------------

Special Instructions:
- For AWS EC2 deployment, ensure port 5000 is open in the security group.
- Use the EC2 public IP for client connections from outside your machine.
