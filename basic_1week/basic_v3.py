a_list = ("키움", "카카오", "대신")

print("\n튜플\n")
## 튜플 - 고정된 값, 속도 빠름, 수정 불가(불변)
for val in a_list:
    print(val)

a_list = ["키움", "카카오", "네이버"]
a_list.append("대신증권")

print("\n리스트\n")
## 리스트
for val in a_list:
    print(val)

print(a_list[0])
print(a_list[-1])  # 리스트의 마지막 부터 센다.

del a_list[1]  # 요소 삭제

for val in a_list:
    print(val)

# enumerate : 인덱스와 함께 순회할 때 사용함
for idx, val in enumerate(a_list):
    print("인덱스 : %s, 값 : %s" % (idx, val))

# 딕셔너리
print("\n딕셔너리\n")
a_dict = {
    "키움증권": 1300,
    "카카오증권": 1500,
    "네이버증권": 1000
}

print(a_dict.get("키움증권"))
print(a_dict["키움증권"])  # get 과 동일하다.
# print(a_dict["키움증권213"]) # 존재하지 않는 키를 입력시 예외(KeyError)가 발생한다.

# 딕셔너리의 순회
for key in a_dict.keys():
    print(a_dict.get(key))
    print(a_dict[key])

# 키와 값을 순회
for key, value in a_dict.items():
    print("키 : %s, 값 : %s" % (key, value))

# 키 추가
a_dict["종호증권"] = 3000
a_dict.update({"연주증권": 4000})

for key, value in a_dict.items():
    print("키 : %s, 값 : %s" % (key, value))

a_dict.update({"퍼뚱증권": 5000, "먹뚱증권": 6999})  # update api는 여러개를 업데이트 할 수 있다.

for key, value in a_dict.items():
    print("키 : %s, 값 : %s" % (key, value))
