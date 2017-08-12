# -*- coding: utf-8 -*-
import os
'''
Created on 8th Aug
This module is for calculating the maximum product of three elements in a sequence
'''

# Split a sequence into three parts including negative, zero and positive
def judgePoNe(sequence):
	# define three list variable
	neg = []
	pos = []
	zero = []
	for i in sequence:
		if i > 0 :
			pos.append(i)
		elif i < 0 :
			neg.append(i)
		else:
			zero.append(i)
	return neg, pos, zero

# To find out the max product of specific number of elements in sequence given
# the elements of given sequence is all positive or negative
def maxPro(sequence, num):
	absSqu = sorted(map(abs, sequence), reverse=True)
	product = 1
	for i in absSqu[0:num]:
		product *= i
	return product


if __name__ == '__main__':
	a = [3, 5, 1, 2, 0, -1, -2,-1,-2]
	# absa = map(abs, a)
	neg, pos, zero = judgePoNe(a)
	if len(neg) <=1:
		print "max product is " + str(maxPro(pos, 3))
	else:
		pro_pos = maxPro(pos, 3)
		pro_neg = maxPro(neg, 2) * max(pos)
		if pro_pos >= pro_neg:
			print "max product is " + str(pro_pos)
		else:
			print "max product is " + str(pro_neg)