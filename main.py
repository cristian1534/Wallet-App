from frontend.home_screen import home
from database.db import Client
from helpers.clear_console import clear_console
import socket


if __name__ == "__main__":
    clear_console()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 9090))

    message = s.recv(2048)
    print(message)
    Client.client_db_connection()
    home()
