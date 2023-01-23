from peewee import *
from database.db import Client
from frontend.menu import menu
from helpers.clear_console import clear_console


class Auth:
    '''
    REGISTER
    '''
    def register(self, Username, Email, Password, Account):
        self.Username = Username
        self.Email = Email
        self.Password = Password
        self.Account = Account

        if len(self.Password) >= 8:
            try:

                self.new_client = Client(
                    Username=self.Username,
                    Email=self.Email,
                    Password=self.Password,
                    Account=self.Account
                )
                self.new_client.save()
                clear_console()
                menu()

            except Exception as e:
                print(e)

        else:
            print("PASSWORD MUST BE MIN 8 LENGTH.")
            return
        
        

    '''
    LOG IN
    '''
    def log_in(self, Password):
        try:
            self.Password = Password
            self.logged = Client.select().where(Client.Password == self.Password)
            if self.logged:
                clear_console()
                menu()
            else:
                print("WRONG PASSWORD...!")

        except Exception as e:
            print(e)
