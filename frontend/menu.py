from decorators.loader import loader
from controllers.account import Account
from helpers.clear_console import clear_console

account = Account()


@loader
def menu():
    while True:
        print('''
            WELCOME TO MACH BANKING APP  
            
            MENU:
            
            1 - CHECK YOUR ACCOUNT.
            2 - DEPOSIT MONEY
            3 - TRANSFER MONEY.
            4 - LOG OUT
            ''')

        option = input('Select OPTION to continue: ')

        if option == "1":
            Password = input("Enter your PASSWORD: ")

            account.fetch_account(Password)

        if option == "2":
            clear_console()
            Amount = int(input("How much money to DEPOSIT? : "))
            Password = input("Enter your PASSWORD: ")

            account.deposit_account(Amount, Password)

        if option == "3":
            clear_console()
            Amount = int(input("How much money to TRANSFER? : "))
            Password = input("Enter your PASSWORD: ")

            account.transfer_money(Amount, Password)

        if option == "4":
           menu()
