def fib():
    prv = 0
    cur = 1
    while 1:
        yield cur
        cur, prv = cur+prv, cur

f = fib()
for i in range(10):
    print(next(f))
