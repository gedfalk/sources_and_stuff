# Given a binary array nums, return the maximum number of consecutive 1's in the array.

nums = [1, 1, 0, 1, 1, 1]

def find(nums):
	_cons, N = 0, 0
	for n in nums:
		if n == 1:
			N += 1
		else:
			if N > _cons:
				_cons = N
			N = 0

	if N > _cons:
		_cons = N
	return(_cons)


print(find(nums))	