# -*- coding:utf-8 -*-
import math
def quadratic(a,b,c):
	
	p = b*b - 4*a*c

	x1 = (-b+math.sqrt(p))/(2*a)

	x2 = (-b-math.sqrt(p))/(2*a)

	return x1,x2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))