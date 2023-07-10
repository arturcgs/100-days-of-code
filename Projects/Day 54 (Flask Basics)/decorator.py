import time


def decorator_function(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@decorator_function
def say_hello():
    print("Hello")


say_hello()