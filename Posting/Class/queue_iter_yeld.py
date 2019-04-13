class queue:
    def __init__(self):
        self.items = []
    def __iter__(self):
        return self
    def __next__(self):
        return self.items.pop(0)
    def push(self, item):
        self.items.append(item)
        return item
def fib():
    prv, cur = 0, 1
    while 1:
        yield cur
        cur, prv = cur+prv, cur
s = stack()
f = fib()
for i in range(10):
    print(s.push(next(f)))
for i in range(10):
    print(next(s))
