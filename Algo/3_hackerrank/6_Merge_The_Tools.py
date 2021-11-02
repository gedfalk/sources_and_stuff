# Разбить строку S на подстроки длиной K и "урезать до основных букв"

s = 'AABCAAADA'
k = 3

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        s1 = string[i:i+k]
        s2 = ''
        for ch in s1:
            if ch not in s2:
                s2 += ch
        
        print(s2)

merge_the_tools(s, k)