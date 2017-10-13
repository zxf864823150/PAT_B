#!/usr/bin./env python3
#PAT提示有返会非0问题= =
import sys
def P(a,b):
    if length < 1 or length > 100:
        return 0
    if diff < 0:
        return 0
    else:
        return True
length,diff = map(eval,input().split(' '))
if P(length,diff):
    length = length
    diff = diff
    try:
        num_list = list(map(eval, input().split(' ')))
        zi_list = num_list[-diff:]
        new_num_list = list(set(num_list).difference(set(zi_list)))
        answer_list = zi_list + new_num_list
        for i in range(len(answer_list)):
            if i == len(answer_list) - 1:
                print(answer_list[i], end='')
            else:
                print('%d ' % answer_list[i], end='')
    except Exception as e :
        sys.exit("error")