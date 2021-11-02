class PositiveList(list):
    def append(self, x):
        if x >= 0:
            list.append(self, x)
        else:
            raise NonPositiveError()
    pass

class NonPositiveError(Exception):
    pass

l = PositiveList()
l.extend([1, 2, 3, 4, 5])
l.append(-6)

print(l)