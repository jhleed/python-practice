# 조건문

stock_name = "키움증권"
if stock_name == "키움증권":
    print("통과")

stock_price = 2000

if stock_price > 3000:
    print("if")
elif stock_price >= 3000:
    print("elif")
else:
    print("else")

stock_price = 3000

if stock_price > 2000 or stock_price < 2500:
    print("2000~2500 사이")
elif stock_price >= 2500 and stock_price <= 3000:
    print("2500~3000 사이")

# 반복문

## for

for i in range(0, 10):
    print(i)

for i in range(5, 100):
    print(i)

    if i == 50:
        break

for i in range(0, 10):
    for k in range(0, 5):
        print("for 문 안에 있는 for 문 %s" % k)

## while

stock_buy = True
count = 0
while stock_price:
    count += 1

    if count == 10:
        break

    print(count)
