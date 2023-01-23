def loader(fn):
    def wrapper(*args):
        try:

            fn(*args)

            print("""
    --------->  LOADING...
                """)
        except Exception as e:
            print(e)

    return wrapper
