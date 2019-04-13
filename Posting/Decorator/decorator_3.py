from functools import wraps
def deco_func_1(func):
    @wraps(func)
    def wrap_func():
        print('Waiting..1', func.__name__)
        return func()
    return wrap_func

def deco_func_2(func):
    @wraps(func)
    def wrap_func():
        print('Waiting..2', func.__name__)
        return func()
    return wrap_func

@deco_func_1
@deco_func_2
def test_func():
    print('Hello World')

test_func()
