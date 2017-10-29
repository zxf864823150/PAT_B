def A_1(a):
    a_1 = []
    a1_sum = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            a_1.append(a[i])
    for j in range(len(a_1)):
        if a_1[j] % 5 == 0:
            a1_sum+=a_1[j]
    if a1_sum == 0:
        return 'N'
    else:
        return a1_sum

def A_2(a):
    a_2 = []
    a2_sum = 0
    for i in range(len(a)):
        if a[i] % 5 == 1:
            a_2.append(a[i])
    a_2_len = len(a_2)
    #print(a_2)
    if a_2_len == 0:
        return 'N'
    else:
        if a_2_len == 1:
            a2_sum = a_2[0]
        elif a_2_len % 2 == 0:
            for h in range(int(a_2_len//2.0)):
                temp = a_2[2*h] - a_2[2*h+1]
                a2_sum+=temp
            #a2_sum+=a_2[-1]
            #print(a2_sum)
        else:
            for i in range(int(a_2_len//2)):
                temp = a_2[2 * i] - a_2[2 * i + 1]
                a2_sum += temp
            a2_sum += a_2[-1]
            #print(a2_sum)
        return a2_sum

def A_3(a):
    count = 0
    for i in range(len(a)):
        if a[i] % 5 == 2:
            count+=1
    if count == 0:
        return 'N'
    else:
        return count

def A_4(a):
    a_4 = []
    a3_sum = 0
    for i in range(len(a)):
        if a[i] % 5 == 3:
            a_4.append(a[i])
    if len(a_4) == 0:
        return 'N'
    else:
        for j in range(len(a_4)):
            a3_sum+=a_4[j]
            avg_a3 = a3_sum/len(a_4)
        return avg_a3

def A_5(a):
    a_5 =[]
    for i in range(len(a)):
        if a[i] % 5 ==4:
            a_5.append(a[i])
    if len(a_5) == 0:
        return 'N'
    else:
        return max(a_5)

num = list(map(eval,input().split(' ')))
num_0 =num[0]
if num_0 <= 0 or num_0 >1000:
    print(None)
for i in range(len(num[1:])):
    if num[i] <=0 or num[i] > 1000:
        tip = 0
    else:
        tip =1
if tip == 0:
    print(None)
else:
    test_list = num[1:]
    a_1 = A_1(test_list)
    a_2 = A_2(test_list)
    a_3 = A_3(test_list)
    a_4 = A_4(test_list)
    a_5 = A_5(test_list)
    if type(a_1) is int:
        print('%d '%a_1,end='')
    else:
        print('%s '%a_1,end='')
    if type(a_2) is int:
        print('%d '%a_2,end='')
    else:
        print('%s '%a_2,end='')
    if type(a_3) is int:
        print('%d '%a_3,end='')
    else:
        print('%s '%a_3,end='')
    if type(a_4) is float:
        print('%.1f '%a_4,end='')
    else:
        print('%s '%a_4,end='')
    if type(a_5) is int:
        print('%d'%a_5,end='')
    else:
        print('%s'%a_5,end='')