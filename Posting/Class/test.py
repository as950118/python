class Person:
    def __init__(self):
        self._name = '홍길동'
    def info(self):
        print("제 이름은 " + self._name + "입니다.")

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, newname):
        self._name = newname

if __name__ == "__main__":# main namespace를 의미합니다.
    customer_1 = Person()#Person의 객체 customer 생성
    customer_2 = Person()
    customer_2.name = "정헌진"
    customer_1.info()
    customer_2.info()
