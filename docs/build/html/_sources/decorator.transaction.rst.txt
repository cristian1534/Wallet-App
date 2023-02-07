DECORATOR
========

DECORATOR:
------------

DECORATOR.TRANSACTION:

.. code-block:: 


import frontend.menu as values
from datetime import datetime


def transactions(fn):
    def wrapper(*args):
        try:
            
            date = datetime.now()
            data = values.Amount

            transaction_details = f"Details of last Transaction: \n- Ammount handled: {data}, Date of operation: {date}"
            f = open("Transactions.txt", "w")
            f.write(str(transaction_details))
            f.close()

            fn(*args)
        except Exception as e:
            print(e)
    return wrapper
