import math as ma
### 牛客网通过，pat显示一个超时
def P(a):
    num = ma.sqrt(a)
    tip_num = int(num)+1
    for i in range(2,tip_num):
        if a % i == 0:
            return 0
    else:
        return a

def D(a):
    count = len(a)//10
    #print(count)
    lost_count = len(a)%10
    loss_list = a[-lost_count:]
    #print(loss_list)
    start = 0
    for i in range(1,count+1):
        for j in range(start,int(i*10)):
            if j ==int(i*10)-1:
                print(a[j])
            else:
                print('%d '%a[j],end='')
        start = i*10
    for h in range(len(loss_list)):
        if h == len(loss_list)-1:
            print(loss_list[h],end='')
        else:
            print('%d '%loss_list[h],end='')
    return 0

num_list = list(map(eval,input().split(' ')))
if num_list[0] > num_list[1] or num_list[0] < 0 or num_list[1] <0 \
    or  num_list[1] > pow(10,4) or type(num_list[0]) != int or type(num_list[1]) != int :
    print(None)
else:
    answer_list = []
    count = 0
    start = 1
    while count < num_list[1]+1:
        num = P(start)
        if num == 0:
            pass
        else:
            answer_list.append(start)
            count += 1
        start+=1

new_anslist = answer_list[num_list[0]:num_list[1]+1]
D(new_anslist)