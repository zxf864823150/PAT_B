#!/usr/bin./env python3
def J(number):
	if number !=1:
		number = (3*number+1)/2.0
	return number

def O(number):
	if number !=1:
		number = number/2.0
	return number

number = eval(input())
if number > 1000:
	print(None)
count = 0
while number !=1:
	if number%2.0==0:
		number = O(number)
		count+=1
	else:
		number = J(number)
		count+=1
print(count)