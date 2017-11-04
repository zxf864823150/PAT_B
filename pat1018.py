### 最后一个测试点超时
def COM(a,b):
    if a != 'J' and b != 'J':
        if a < b:
            return 1
        elif a==b:
            return 0
        else:
            return 2
    elif a == 'J':
        if b == 'J':
            return 0
        elif b == 'B':
            return 1
        else:
            return 2
    elif b == 'J':
        if a == 'J':
            return 0
        elif a == 'B':
            return 2
        else:
            return 1
    return

def MAX_F(a):
    temp_list =[]
    B_count = a.count('B')
    temp_list.append((B_count))
    C_count = a.count('C')
    temp_list.append(C_count)
    J_count = a.count('J')
    temp_list.append(J_count)
    for i in range(len(temp_list)):
        if temp_list[i] == max(temp_list):
            answer = i
            break
    return answer
def P_A(a):
    if a == 0:
        return 'B'
    elif a == 1:
        return 'C'
    elif a == 2:
        return 'J'
    return

num = eval(input())
if num < 0 or num >pow(10,5):
    print(None)
else:
    A_list =[]
    B_list = []
    A_count = 0
    B_count = 0
    P_count = 0
    A_answer = []
    B_answer = []
    for i in range(num):
        a,b = input().split(' ')
        A_list.append(a)
        B_list.append(b)
    for j in range(len(A_list)):
        tip = COM(A_list[j],B_list[j])
        if tip == 1:
            A_count+=1
            A_answer.append(A_list[j])
        elif tip == 2:
            B_count+=1
            B_answer.append(B_list[j])
        elif tip == 0:
            P_count+=1
    A_FU = num - (A_count+P_count)
    B_FU = num -(B_count+P_count)
    print('%d '%A_count+'%d '%P_count+'%d'%A_FU)
    print('%d '%B_count+'%d '%P_count+'%d'%B_FU)
    A_most = MAX_F(A_answer)
    B_most = MAX_F(B_answer)
    A_N = P_A(A_most)
    B_N = P_A(B_most)
    print(A_N+' '+B_N)