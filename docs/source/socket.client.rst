SOCKET
========

SOCKET:
------------

SOCKET.CLIENT:

.. code-block:: 

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 9090))

message = s.recv(2048)
print(message)