def calc(*numbers):
	sum = 0 
	for n in numbers:
		sum = sum + n * n
	return sum

name = [1,3,5,7]
print(calc(*name))