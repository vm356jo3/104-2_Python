#!/usr/bin/env python
# -*- coding: utf-8 -*-
def isPrime(N):
	prime=1
	for x in range(1,N,2):
		for y in range(2,x):
			if N%y==0:
				prime=0
				break
	if prime==0:
		return 0
	else:
		return 1
sum=0
print u'1000以內的質數：'
for x in range(2,1000):
	if isPrime(x)==1:
		print x
		sum=sum+x
print u'所有1000以內的質數總合為：'
print sum