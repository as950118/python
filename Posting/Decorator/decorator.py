def deco_func(func):
    def wrap_func():
        return func()
    return wrap_func

def test_func():
    print('Hello World')

@deco_func
def test_func_2():
    print("decorator")

deco_test = deco_func(test_func)
deco_test()

test_func_2()
