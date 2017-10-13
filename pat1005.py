#!/usr/bin./env 
import time
def J(number):
	if number !=1:
		number = (3*number+1)/2.0
	return number

def O(number):
	if number !=1:
		number = number/2.0
	return number

def S(number):
	count = []
	while number !=1:
		if number%2.0==0:
			number = O(number)
			count.append(number)
		else:
			number = J(number)
			count.append(number)
	return count
def G(a=[],b=[]):
	c = []
	for i in range(len(a)):
		if a[i] not in b:
			c.append(a[i])
	return c

number = eval(input())
number_list = list(map(eval,input().split(' ')))
start_t = time.time()
if number >= 100:
	print(None)
all_list = []
for i in range(len(number_list)):
	temp = S(number_list[i])
	all_list.extend(temp)
	all_list = list(set(all_list))###为了加速
	#temp0 = G(number_list,all_list)
	#number_list = temp0
### 直接使用字典的差集更快
h = list(set(number_list).difference(set(all_list)))
'''
answer_list = sorted(temp0)
answer_list.reverse()
for i in range(len(answer_list)):
	if i == len(answer_list)-1:
		print(answer_list[i],end='')
	else:
		print('%d '%answer_list[i],end='')
'''
h = sorted(h)
h.reverse()
for i in range(len(h)):
	if i == len(h)-1:
		print(h[i],end='')
	else:
		print('%d '%h[i],end='')
end_t = time.time()
print(end_t-start_t)