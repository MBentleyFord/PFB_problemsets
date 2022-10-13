#!/usr/bin/env python3

def factorial(n):
	num=1
	while n>=1:
		num=num*n
		n=n-1
	return num
f=factorial(1000)
print(f)

