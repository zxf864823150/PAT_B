def P(a,b,c,i):
    if a+b > c:
        a = 'Case #%d: true'%(i+1)
    else:
        a = 'Case #%d: false'%(i+1)
    return a

num = eval(input())
answer_list = []
if num <=0 or num >10:
    print(None)
else:
    for i in range(num):
        l = list(map(eval,input().split(' ')))
        a = l[0]
        b = l[1]
        c = l[2]
        if a not in range(pow(-2,31),pow(2,31)+1) or b not in range(pow(-2,31),pow(2,31)+1) or\
                        c not in range(pow(-2,31),pow(2,31)+1):
            print(None)
        answer = P(a,b,c,i)
        answer_list.append(answer)
    for j in range(len(answer_list)):
        if j == len(answer_list)+1:
            print(answer_list[j],end='')
        else:
            print(answer_list[j])