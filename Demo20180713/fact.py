def fact(n):
	if n==1:
		return 1
	return n * fact(n-1)

print(fact(5))


def factA(num,product):
	if num == 1:
		return product
	return factA(num - 1, num * product)

print(factA(100,1))
	
	