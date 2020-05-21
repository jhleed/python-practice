print("Hello world")
print("Hello world" + " Thank you")
print(900629)

print("%s 입니다." % "홍길동")
print("%s 입니다." % "이순신")
print("%s 원 입니다." % 5000)

print("이름은 %s 이고 %s 에 삽니다." % ("홍길동", "서울"))  # %의 개수에 맞게 인자를 줘야 한다.

# 변수

## int 타입
stock_price = 3900
print(stock_price)

stock_price_type = type(stock_price)  # 변수의 타입 확인
print(stock_price_type)

## float 타입
stock_percent = 3.8
print(stock_percent)
stock_percent_type = type(stock_percent)
print(stock_percent_type)

## str 타입
stock_name = "홀딩스"
print(stock_name)
stock_name_type = type(stock_name)
print(stock_name_type)

## bool 타입
stock_buy = False
print(stock_buy)
stock_buy_type = type(stock_buy)
print(stock_buy_type)

# 산술 연산

## 덧셈
stock_price = 2000
stock_price2 = 2500
stock_result = stock_price + stock_price2
print(stock_result)

## 뺄셈
stock_result = stock_price - stock_price2
print(stock_result)

## 곱셈
stock_result = stock_price * stock_price2
print(stock_result)

## 나눗셈
stock_result = stock_price2 / stock_price
print(stock_result)
print(int(stock_result))
stock_result = stock_price2 // stock_price
print(stock_result)  # // 기호는 소숫점을 버리고, 정수형인 Int 타입으로 변환한다. int(stock_result)와 동일하다.

## 나머지 연산
stock_result = stock_price2 % stock_price
print(stock_result)
