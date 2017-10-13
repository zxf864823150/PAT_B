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
count = 0
for i in range(5,amount+1):
	if Z(i-2) and Z(i):
		count+= 1
print(count)
end = time.time()
print((end-start)*1000)

