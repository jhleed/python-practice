class B_school():

    # 지정함수, 클래스가 생성될 때 초기화
    def __init__(self):
        print("b 대학교 초기화")


B_school()


class A_school():

    def __init__(self):
        print("초기화, 생성자")
        self.student1_name = None

        b = self.math()
        print("수학과 학생 %s" % b)
        print(self.student1_name)

        # dir 은 매개변수로 전달된 정보에 어떤 데이터가 있는지 보여준다.
        print(dir(self))

    def math(self):
        self.student1_name = "영수"
        name = self.student1_name
        return name


A_school()
