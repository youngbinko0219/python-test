import time
from datetime import date, datetime, timedelta

# 오늘 날짜 출력
today = date.today()
print('오늘 날짜:', today, today.year, today.month, today.day)

print("=" * 30)

# 현재 시각 출력
dtime = datetime.now()
print('현재 시각:', dtime)
print('년/월/일:', dtime.year, dtime.month, dtime.day)
print('시/분/초/밀리세컨드:', dtime.hour, dtime.minute, dtime.second, dtime.microsecond)

print("=" * 30)

# 날짜 계산 1
one_day = timedelta(days=1)
yesterday = today - one_day
tomorrow = today + one_day
print("어제와 오늘:", yesterday, tomorrow)

# 날짜 계산 2
date_diff = today - yesterday
print("날짜 차이:", date_diff)

# 날짜 형식 변환
date_str = today.strftime('%Y-%m-%d')
print("형식 지정:", date_str)

# 크리스마스까지 남은 날짜 계산
x_mas_str = f'{today.year}-12-25'
x_mas_datetime = datetime.strptime(x_mas_str, '%Y-%m-%d')
x_mas_date = datetime.date(x_mas_datetime)

print(x_mas_str, x_mas_datetime, x_mas_date)
print(type(x_mas_str), type(x_mas_datetime), type(x_mas_date))

date_diff = x_mas_date - today
print("크리스마스까지:", date_diff)
print("크리스마스까지 (일):", date_diff.days)
