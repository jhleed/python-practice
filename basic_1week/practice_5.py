class Kiwoom():
    def __init__(self):
        self.dic = {
            "네이버": 6000,
            "애플": 15000,
            "다음": 3000,
            "넷플릭스": 5000
        }


class Condition():
    def __init__(self):
        pass

    # condition 클래스에서 5000원 이하의 종목들만 출력
    def sell_filtering(self):
        result = []
        kiwoom = Kiwoom()

        result = []

        for key, value in kiwoom.dic.items():
            if value <= 5000:
                result.append({key: value})

        return result


print(Condition().sell_filtering())
