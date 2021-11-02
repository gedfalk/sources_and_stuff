# Работа с файловой системой и файлами
# Рекурсивный перебор директорий с целью поиска тех, в которых есть хотя
# бы один файл с расширением .py

import os
import os.path

data = []

for cd, d, f in os.walk('.'):
    for ff in f:
        if ff[-3::] == '.py' and cd not in data:
            data.append(cd)

for s in sorted(data):
    print(s[2::])
