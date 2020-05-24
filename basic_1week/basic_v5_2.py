class Parent():
    def __init__(self):
        print("부모입니다.")

        self.money = 5000000

    def home(self):
        return "부모의 집"


class ChildA(Parent):
    def __init__(self):
        print("자식 A")

        print("부모의 돈을 물려받을 수 없습니다.")
        print("%s을 물려받았습니다." % self.home())


class ChildB(Parent):
    def __init__(self):
        super().__init__()  # super 가 사용 가능하구나. 근데 init 만 되네? -> 부모 생성자 사용 용도인가보다?
        print("자식 B")

        # print("부모의 돈 %s" % super().money)
        print("부모의 돈 %s" % self.money)
        print("%s을 물려받았습니다." % self.home())


# Parent()
# ChildA()
ChildB()
