from frontend.home_screen import home
from database.db import Client






if __name__== "__main__":
    Client.client_db_connection()
    home()