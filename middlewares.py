import os

def console_clear(func):
    def wrapper(*args, **kwargs):
        os.system('cls')

        result = func(*args, **kwargs)

        input('Operation was finished.\nPress Enter to continue.')
        os.system('cls')

        return result
    return wrapper