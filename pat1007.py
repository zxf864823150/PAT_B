#!/usr/bin./env python3
import math as ma
import time
def Z(number):
	num = ma.sqrt(number)
	#print(num)
	for i in range(2,int(num+1)):
		if number%i == 0:
			return 0
			break
	return True

amount = eval(input())
start = time.time()
if amount >= ma.pow(10,5):
	print(None)
zhi_number = []
count = 0
for i in range(2,amount+1):
	temp = Z(i)
	if temp != 0:
		zhi_number.append(i)
#print(zhi_number)
for i in range(len(zhi_number)-1):
	for j in range(i,len(zhi_number)):
		if abs(zhi_number[i]-zhi_number[j]) == 2:
			#print('%d,%d'%(i,j))
			count+=1
print(count)
end = time.time()
print((end-start)*1000)

