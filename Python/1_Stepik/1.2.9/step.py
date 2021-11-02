objects = [1, 2, 1, 2, 3]
final = []

result = 0
for o in objects:
  if o not in final:
    final.append(o)
    result += 1

print(result, final)




