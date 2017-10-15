#!/usr/bin/env python3
# 测试点1 和2 错误不知道为什么
import sys
def P(num):
    for i in range(len(num)):
        if abs(num[i]) >1000:
            return 0
        else:
            return True

def D(a,b):
    if b == 0:
        return 0,0
    else:
        return a*b,b-1
try:
    num_list = list(map(eval,input().split(' ')))
    l = P(num_list)
    if l == 0:
        print(None)
    length = len(num_list)
    leng_num = length/2.0
    ### 输入全为常数项时
    if num_list == [0,0]:
        print('%d %d'%(0,0),end='')
    zero_num = num_list.count(0)
    if zero_num == leng_num:
        for i in range(leng_num):
            if i == leng_num-1:
                print('%d %d'%(0,0),end='')
            else:
                print('%d %d '%(0,0),end='')
    ###
    answer_list = []
    for i in range(int(leng_num)):
        xi,dao = D(num_list[2*i],num_list[2*i+1])
        temp_list = [xi,dao]
        if xi==dao==0:
            pass
        else:
            answer_list.extend(temp_list)
    for i in range(len(answer_list)):
        if i == len(answer_list)-1:
            print('%d'%answer_list[i],end='')
            break
        print('%d '%answer_list[i],end='')
except Exception as e:
    print('%d %d'%(0,0),end='')
#sys.exit(0)