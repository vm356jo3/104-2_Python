#! /usr/bin/env python
# -*- coding: utf-8 -*-
#   ch6_hw1.py
class Professor:
	mantra=u"我一點都不會介意XD"
	def __init__(self,name):
		self.name = name
		
	def dosomething(self,specialty):
		self.specialty = specialty
		print self.name,
		print u"的專長為",
		print self.specialty
		
class Student(Professor):
	def dosomehobby(self,hobby):
		self.hobby = hobby
		print self.name,
		print u"的興趣為",
		print self.hobby
		
a=Professor(u"教授")
a.dosomething(u"C語言")
a.dosomething(u"電腦網路")
b=Student(u"學生")
b.dosomething(u"C語言")
b.dosomething(u"電腦網路")
b.dosomehobby("Python")
print a.mantra
print b.mantra