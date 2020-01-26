def decorator_function(func):
    def wrapper_function():
        print("This was wrapped")
        return func()
    return wrapper_function


@decorator_function
def wrapper_checker():
    print("Checked")