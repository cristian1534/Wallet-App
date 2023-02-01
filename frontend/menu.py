from controllers.account import Account
from helpers.clear_console import clear_console
from decorators.loader import loader


account = Account()

@loader
def menu():
    global Amount

    while True:
        try:
            print('''
                WELCOME TO MACH BANKING APP  
                
                MENU:
                
                1 - CHECK YOUR ACCOUNT.
                2 - DEPOSIT MONEY
                3 - TRANSFER MONEY.
                4 - RECEIVE OF LAST OPERATION.
                5 - LOG OUT
                ''')

            option = input('Select OPTION to continue: ')

            if option == "1":
                clear_console()
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
                account.print_receive()

            if option == "5":
                clear_console()
                break
        except Exception as e:
            print(e)
