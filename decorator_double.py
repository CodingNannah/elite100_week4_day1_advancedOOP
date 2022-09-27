def decorator(func):
    def inner():
        print("before the func is called")
        func()
        print("after the function is called")
    return inner

@decorator
@decorator
def my_func():
    print("This is inside the function")


my_func()
# decorator(my_func)()