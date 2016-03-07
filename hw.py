#!usr/bin/env python
# -*- coding: utf-8 -*-
f = open("ATM.txt","a")
account=5000
print u'您的帳戶餘額為 NT$5000 元。'
f.write("您的帳戶餘額為 NT$5000 元。\n")
print u'請輸入欲領金額：'
f.write("請輸入欲領金額：\n")
want=input()
f.write("%d\n" %(want))
if account-want<0:
	print u'您的存款不足！'
	f.write("您的存款不足！\n\n")
	f.close()
elif account-want==0:
	print u'您的存款無剩餘存款。'
	f.write("您的存款無剩餘存款。\n\n")
	f.close()
else:
	print u'您的存款還剩 NT$%d 元。' %(account-want)
	f.write("您的存款還剩 NT$%d 元。\n\n" %(account-want))
	f.close()