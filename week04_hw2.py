#!/usr/bin/env python
# -*- coding: utf-8 -*-
print u'請輸入一數字：'
num=input()
for x in range(1,num,2):
	prime=1
	for y in range(2,x):
		if num%y==0:
			prime=0
			break
if prime==0:
	print u'%d不是質數。' %num
else:
	print u'%d是質數。' %num