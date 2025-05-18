class Test:
    count = 0
    def __new__(cls, *args, **kwargs):
        cls.count += 1
        return super().__new__(cls)

    def __init__(self, a):
        self.a = a

    @staticmethod
    def get_count():
        print(Test.count)


t1 = Test(1)

t2 = Test(5)
Test.get_count()
print(t2.a)
