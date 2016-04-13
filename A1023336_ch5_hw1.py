#! /usr/bin/env python
# -*- coding: utf-8 -*-
#   ch5_hw1.py
import re
print u"請輸入您的會員卡號："
username=raw_input()
while re.findall(r"[A-Z]-\d{6}",username)==[]:
	print u"卡號格式錯誤，正確格式為1個大寫英文字-6碼數字，請重新輸入："
	username=raw_input()
if re.findall(r"E-056790",username)!=[]:
	print u'恭喜您中了10萬元。'
elif re.findall(r"E-[\d]{1}56790",username)!=[]:
	print u'恭喜您中了2萬元。'
elif re.findall(r"[A-Z]-[\d]{3}790",username)!=[]:
	print u'恭喜您中了100元。'
else:
	print u'銘謝惠顧。'
