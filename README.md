Project: Simple FTP Server and Client
------------------------------------

Collaborators: 

Bryan Tran | Email: btran299@csu.fullerton.edu\
Peter Chau | Email: Peterchauu93@csu.fullerton.edu

Language: Python 3  

Description:
This project implements a simple file transfer system using socket programming in Python.
It allows the client to connect to the server and perform basic FTP-like commands:
- ls   : list files on the server
- get  : download a file from the server
- put  : upload a file to the server
- quit : disconnect from the server

------------------------------------

How to Run:

1. Open two terminals.
2. In the first terminal, start the server:
   python3 server.py
3. In the second terminal, start the client:
   python3 client.py
4. Once connected, you can type commands such as:
   ftp> ls
   ftp> get test1.txt
   ftp> put newfile.txt
   ftp> quit

------------------------------------

Notes:
- Make sure both `server.py` and `client.py` are in the same folder.
- You can add any test files (like test1.txt) to the same folder to test file transfer.
- The server should be started before the client.
- The client connects to localhost (127.0.0.1) using port 12345.

------------------------------------

Special Instructions:
None.
