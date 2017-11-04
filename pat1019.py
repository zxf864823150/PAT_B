###坑：3要转变为0003处理，考虑中间步骤会产生类似的情况要补全
###测试点3过不去，求指点
def P_A(a):
    Ascend_list = sorted(a)
    small_num = Ascend_list[0]
    Down_list = Ascend_list[::-1]
    big_num = Down_list[0]
    for i in range(1,len(Ascend_list)):
        small_num+=Ascend_list[i]
    for j in range(1,len(Down_list)):
        big_num+=Down_list[j]
    answer_num = int(big_num) - int(small_num)
    print(big_num+' - '+small_num+' = '+'%d'%answer_num)
    return answer_num
num = input()
if int(num) not in range(1,10001):
    print(None)
else:
    if len(num) < 4:
        for i in range(len(num),4):
            num+='0'
    temp = list(set(num))
    if len(temp) == 1:
        print(num+' - '+num+' = 0000')
    else:
        if num == '6147':
            print(None)
        else:
            tip = P_A(num)
            while tip != 6174:
                new_tip = str(tip)
                if len(new_tip)<4:
                    for i in range(len(new_tip), 4):
                        new_tip += '0'
                ans = P_A(new_tip)
                tip =ans


