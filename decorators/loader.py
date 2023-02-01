def loader(fn):
    def wrapper(*args):
        try:

            fn(*args)

            print("""
////////////////////////////// --> Closing session...
                """)
        except Exception as e:
            print(e)

    return wrapper
