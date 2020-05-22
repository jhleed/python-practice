from yahoo_finance import Share

# https://minjejeon.github.io/learningstock/2016/07/12/getting-data-from-yahoo-finance.html
samsung = Share("005930.KS")
print(samsung.get_info())
