#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
f = open("input.txt")
article=[]
for line in f:
	article.extend(line)
num3=len(article)
print u'在此文字檔中：'
num1=article.count(' ')
print u'空白鍵共出現 %d 次。' %num1
num4=float(num1/num3)
print u'共佔文字檔 %d ' %(num4*100)+'%'
num2=article.count('e')
print u'字母e共出現 %d 次。' %num2
num5=float(num2/num3)
print u'共佔文字檔 %d ' %(num5*100)+'%'
f.close()
