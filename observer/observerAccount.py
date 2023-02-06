

class Observer:
    def __init__(self, Username):
        self.Username = Username
       

    def update(self, message):
        print(f"Client: {self.Username}\nMessage: {message}\n")


class Observer_Account:
    def __init__(self):
        self.transactions = []

    def created_transaction(self, observer):
        self.transactions.append(observer)

    def delete_transaction(self, Amount):
        self.transactions.remove(Amount)

    def dispatch_message(self, message):
        for observer in self.transactions:
            observer.update(message)


