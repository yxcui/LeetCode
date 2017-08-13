# -*- coding: utf-8 -*-
import os
import math
import sys
'''
Created on 11th Aug
This question is from 2017 NetEase Campus Recruit
'''

# calculate all divisors without 1 and self for a given number in the natural range
def calDivisors(N):
	divisors = []
	for i in range(2, int(N / 2.0)+1):
		if N % i == 0:
			divisors.append(i)
	# divisors.append(N)
	return divisors


# this function is mainly besed on recursive method, but works not good
def stepStone(N, M, count):
	count = count + 1
	divisorsN = calDivisors(N)
	divisorsN.pop()
	del divisorsN[0]

	N_next = [e + N for e in divisorsN]

	for ele in N_next:
		if ele < M:
			stepStone(ele, M, count)
			continue
		elif ele == M:
			print count   # print the count while get M
			break

# 
def stepStone1(N, M):
	# init a dictionary to store the count
	stone = {}
	stone[N] = 0
	stoneIndex = {}   # 考虑将最小路径保存下来
	for i in range(N+1, M+1):
		stone[i] = sys.maxint

	if N == M:
		return stone[M]
	else:
		# 针对每一个石块，计算其能到达的石块，然后每个石块都保留了到达此处需要的步数，每次遍历都保留最小值，即最少需要的步数
		for i in range(N, M+1):
			divisors = calDivisors(i)
			for j in divisors:
				if i + j <= M:
					stone[i + j] = min(stone[i] + 1, stone[i + j])
					# stoneIndex[i + j] = i   # 存储到达 i+j 石块的石块编号
		return stone[M], stoneIndex


if __name__ == '__main__':
	# count = 0   # count how many times need from N to M
	# stepStone(4, 24, count)

	stone, stoneIndex = stepStone1(4, 24)
	print stone