# -*- coding: utf-8 -*-
import os
'''
Created on 11th Aug
This question is from 2017 NetEase Campus Recruit
'''

def reverseSingleNo(number):
	strNo = str(number)
	listNo = list(strNo)
	listNo.reverse()   # reverse the list
	strNo1 = "".join(listNo)
	return int(strNo1.lstrip('0'))


if __name__ == '__main__':
	s1 = "123"
	s2 = "100"
	plus = reverseSingleNo(s1) + reverseSingleNo(s2)
	result = reverseSingleNo(plus)
	print "The plus of s1 and s2 after reversing is {0}".format(result)
