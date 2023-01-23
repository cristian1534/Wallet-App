from database.db import Client
from helpers.clear_console import clear_console


class Account:

    def fetch_account(self, Password):
        clear_console()
        try:
            self.Password = Password

            self.account = Client.select().where(Client.Password == self.Password)
            if self.account:
                for amount in self.account:
                    print("CURRENT BALANCE:", amount.Account)
            else:
                print("WRONG PASSWORD..!")

        except Exception as e:
            print(e)

    def deposit_account(self, Amount, Password):
        clear_console()
        try:
            self.Amount = Amount
            self.Password = Password
            self.Cash = []

            current_account = Client.select().where(Client.Password == self.Password)
            for current_amount in current_account:
                self.Cash.append(current_amount.Account)

            self.Cash.append(self.Amount)

            self.updated_amount = sum(self.Cash)

            self.updated_account = Client.update(Account=self.updated_amount).where(
                Client.Password == self.Password).execute()

            if self.updated_account:
                print(f'DEPOSITED SUCCESSFULLY: {self.Amount}')

            else:
                print("COULD NOT GET DEPOSITED.")

        except Exception as e:
            print(e)

    def transfer_money(self, Amount, Password):
        clear_console()
        try:
            self.Amount = Amount
            self.Password = Password
            self.Cash = []

            current_account = Client.select().where(Client.Password == self.Password)
            for current_amount in current_account:
                self.Cash.append(current_amount.Account)

            if self.Cash[0] <= 0 or self.Cash[0] < self.Amount:
                print("NOT ENOUGH MONEY FOR THIS OPERATION.")
            else:
                self.transferred_amount = self.Cash[0] - self.Amount

                self.updated_account = Client.update(Account=self.transferred_amount).where(
                    Client.Password == self.Password).execute()

                if self.updated_account:
                    print(f'TRANSFER SUCCESS: {self.Amount}')

                else:
                    print("COULD NOT TRANSFER.")

        except Exception as e:
            print(e)
