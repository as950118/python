def deco_func(func):
    def wrap_func():
        print('Waiting..1')
        print('Waiting..2')
        print('Waiting..3')
        print('Waiting..4')
        return func()
    return wrap_func

@deco_func
def test_func_1():
    print('Hello World')
@deco_func
def test_func_2():
    print('Hello World')
@deco_func
def test_func_3():
    print('Hello World')
@deco_func
def test_func_4():
    print('Hello World')



test_func_1()
test_func_2()
test_func_3()
test_func_4()
#deco_test = deco_func(test_func)
#deco_test()
