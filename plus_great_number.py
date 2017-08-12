# -*- coding: utf-8 -*-
import os
'''
Created on 8th Aug
This module is for the Product of two great number
'''

# 
def reverseN(lagNum):
	sequence = list(lagNum)
	sequence = map(int, sequence)
	sequence.reverse()
	return sequence

def parseListToLagNum(resultSeq):
	for index in range(len(resultSeq)):
		if resultSeq[index] < 10:
			continue
		else:
			resultSeq[index + 1] += resultSeq[index] / 10
			resultSeq[index] = resultSeq[index] % 10
	resultSeq.reverse()
	return "".join(map(str, resultSeq)).lstrip('0')

def cal2LagNum(num1seq, num2seq):
	result = [0] * (len(num1seq) + len(num2seq))  # To avoid the index of result[i + j] out of range. Tha result length is [len(num1seq) + len(num2seq)] or [len(num1seq) + len(num2seq) - 1]
	for i in range(len(num1seq)):
		for j in range(len(num2seq)):
			if j == len(num2seq) - 1:
				result[i + j] = (num1seq[i] * num2seq[j])
			else:
				before = result[i + j]
				result[i + j] = (num1seq[i] * num2seq[j]) + before   # this can make 0 be replaced by result[i+j]
				# result.append(0)   # To avoid the index of result[i + j] out of range in the next loop 
	return result
	
 
if __name__ == '__main__':
	num1 = "2145"
	num2 = "2335674"
	num1seq = reverseN(num1)
	num2seq = reverseN(num2)
	resultSeq = cal2LagNum(num1seq, num2seq)
	r = parseListToLagNum(resultSeq)
	print "The product of {0} and {1} is {2}.".format(num1, num2, r)