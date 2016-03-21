#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
t=1
answer=random.randint(1,99)
num=[1, answer, 99]
print u'終極密碼, Start!!!'
print u'請輸入你猜的數字>>'
guess=input()
while guess!=answer:
	if answer<guess:
		t=t+1
		print u'現在範圍是%d~%d' %(num[0], guess)
		num[2]=guess
		print u'請輸入你猜的數字>>'
		guess=input()
	if guess<answer:
		t=t+1
		print u'現在範圍是%d~%d' %(guess, num[2])
		num[0]=guess
		print u'請輸入你猜的數字>>'
		guess=input()
print u'恭喜你猜中！終極密碼是%d，你花了%d次猜中。' %(answer, t)