# Работа с кодом: модули и импорт
# Модуль datetime и работа с датами

import datetime

y, m, d = map(int, input().split())
date = datetime.date(y, m, d)

d = int(input())
day = datetime.timedelta(days = d)

result = date + day
print(result.year, result.month, result.day)
