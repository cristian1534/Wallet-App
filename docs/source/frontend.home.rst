FRONTEND
========

FRONTEND:
------------

FRONTEND.HOME:

.. code-block:: 

from controllers.auth import Auth
from helpers.clear_console import clear_console


auth = Auth()


def home():
    while True:
        print('''
              1 - Register
              2 - Log In
              3 - Exit
              ''')

        option = input("Select OPTION: ")

        try:
            if option == "1":
                clear_console()
                print('''
                       COMPLETE TO REGISTER:
                        ''')
                Username = input("Username: ")
                Email = input("Email: ")
                Password = input("Password: ")
                Account = 0

                clear_console()
                auth.register(Username, Email, Password, Account)
               
                

            if option == "2":
                clear_console()
                print('''
                        COMPLETE TO LOGIN:
                        ''')
                Password = input("Password: ")
                
                clear_console()
                auth.log_in(Password)
                

            if option == "3":
                clear_console()
                print("""
                        Thank you for using MACH BANKING APP
                        """)
                break

        except Exception as e:
            print(e)
