def decorator(func):
    def inner():
        print("before the func is called")
        func()
        print("after the function is called")
    return inner

def decorator2(func):
    def inner():
        func()
        print("I did a bunch of cool stuff")

    return inner

@decorator2
@decorator
def my_func():
    print("This is inside the function")


my_func()
# decorator(my_func)()

####################################################################


def add_two(func):
    def inner(x,y):
        return func(x,y)+2
    return inner

@add_two
def my_func(x,y):
    return x+y

print(my_func(3,2))
