#!/usr/bin/env python

### CS 61A  LECTURE 18 

def divides(k,n):
	return n % k == 0

def factors(n):
	total = 0 
	for i in range(1,n+1):
		if divides(i,n):
			total += 1
	return total # 傻逼，return 当然要卸载loop外面

from math import sqrt # 引进开平方

def factors_fast(n):
	total = 0
	sqrt_n = sqrt(n)
	k = 1 
	while k < sqrt_n:
		if divides(k,n):
			total += 2
		k += 1
	if k ==sqrt_n:
		total += 1
	return total 

print(factors_fast(576))

def exp(b,n):
	if n == 0:
		return 1
	else:
		return exp(b,n-1)*b 




