DataBase
========

DB Conection:
------------

CONECTION WITH PEEWEE:

.. code-block:: 

'''
Connection to DataBase
'''
db = SqliteDatabase('Clients')

class Client(Model):
    Username = CharField(50)
    Email = CharField(50)
    Password = CharField(10)
    Account = IntegerField()
    
    class Meta():
        database = db
    
    def client_db_connection():
        try:
            db.create_tables([Client])
            if not db.is_closed():
                db.close()
                print("Connected to DataBase.")
        except Exception as e:
            print(e)
            
 