# Преобразование числа из римской системы

Nums = {5: 'V',
        48: 'XLVIII',
        60: 'LX',
        99: 'XCIX',
        100: 'C',
        75: 'LXXV',
        14: 'XIV'}

num = Nums[14]

print(num)

Rules = {    'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000   }

PRules = {'IV': 4,
          'IX': 9,
          'XL': 40,
          'XC': 90,
          'CD': 400,
          'CM': 900    }

l_num = num
for r, a in PRules:
    if r in num:
        l_num