SOCKET
========

SOCKET:
------------

SOCKET.SERVER:

.. code-block:: 

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9090))
s.listen(5)

while True:
    clientSocket, address = s.accept()
    print(f"CONNECTION ESTABLISHED FROM {address}")
    clientSocket.send(bytes("""WELCOME TO MACH BANKING APP""", "utf-8"))
    clientSocket.close()