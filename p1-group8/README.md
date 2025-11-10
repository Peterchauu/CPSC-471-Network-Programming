Project: Simple FTP Server and Client
------------------------------------

Collaborators: 

Bryan Tran | Email: btran299@csu.fullerton.edu
Peter Chau | Email: Peterchauu93@csu.fullerton.edu

Language: Python 3

------------------------------------

Description:
This project implements a simplified file transfer protocol (FTP) system using socket programming in Python.
It allows a client to connect to the server and perform basic FTP-like operations:

- ls   : list files on the server
- get  : download a file from the server
- put  : upload a file to the server
- quit : disconnect from the server

------------------------------------

How to Run:

1. Open two terminal windows.
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
- You can add test files (like `test1.txt` and `test2.txt`) in the same directory to test file transfer.
- The server must be started before the client.
- The client connects to `localhost (127.0.0.1)` using port **5000**.
- This project was developed and tested using **WSL (Windows Subsystem for Linux) Ubuntu 22.04** on Windows 10/11. The terminal commands (`ls`, `cd`, `python3`) were executed in Ubuntu.

------------------------------------

Special Instructions:
None.

------------------------------------

Tar Instructions (for submission):
Place all your files (server.py, client.py, README.txt, and test files) in one folder named:
   p1-[your_userid]

Then run:
   tar cvf p1-[your_userid].tar p1-[your_userid]

Upload the .tar file to Canvas.