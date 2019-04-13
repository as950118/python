import time

class Cookie:
    var_time = time.asctime(time.localtime())
    def __init__(self):
        self.shape = 'Human'
        #self.time = time.asctime(time.localtime())
    def GetShape(self):
        return self.shape
    #def GetTime(self):
    #    return self.time

cookie_1 = Cookie()
time.sleep(10)
cookie_2 = Cookie()

print(cookie_1.GetShape(), cookie_1.var_time)
print(cookie_2.GetShape(), cookie_2.var_time)
