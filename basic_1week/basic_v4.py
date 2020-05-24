def english():
    print("영어과입니다.")


english()


def match(student_name):
    print(student_name)


match("이종호")


def call_function(func):
    func()


def help():
    print("도와주러 왔습니다.")


call_function(help)


def get_name():
    name = "종호"
    return name


who = get_name()
print(who)


def multi():
    return "a", "b"


a, b = multi()

print(a, b)
