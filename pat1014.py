### 测试点5过不去，显示返回非0，求指点
def Day_HOU(a,b):
    tip_list = []
    day_list = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    time_list = list(map(str,range(10)))
    temp_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
    time_list.extend(temp_list)
    #print(time_list)
    leng = min([len(a),len(b)])
    #print(leng)
    for i in range(leng):
        if a[i] == b[i] and a[i] >= 'A' and a[i] <='G':
            tip_list.append(a[i])
        elif tip_list != [] and a[i] == b[i] and a[i] in time_list:
            tip_list.append(a[i])
    #print(tip_list)
    for i in range(len(temp_list)):
        if temp_list[i] ==tip_list[0]:
            DAY = day_list[i]
    if len(tip_list)>1:
        for j in range(len(time_list)):
            if time_list[j] == tip_list[1]:
                HOU = str(j)
                if len(HOU) == 1:
                    HOU = '0'+HOU
            #print(j)
        return DAY,HOU
    else:
        return DAY,'0'

def GET_MIN(a,b):
    min_len = min(len(a),len(b))
    for i in range(min_len):
        if a[i] == b[i] and a[i].upper() != a[i]:
            MIN = i
            if MIN < 10:
                MIN = '0' + str(i)
            else:
                MIN = str(i)
            break
    #print(MIN)
    return MIN

def NEW_HOU(a,b):
    tip_list = []
    time_list = list(range(10))
    temp_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
    time_list.extend(temp_list)
    #print(time_list)
    leng = min([len(a),len(b)])
    for i in range(leng):
        if a[i] == b[i]:
            new_h = a[i].upper()
            print(new_h)
            break
    for j in range(len(time_list)):
        if time_list[j] == new_h:
            HOU = str(j)
        else:
            HOU = '0'
    return HOU

#for i in range(4):
Day_In1 = input()
Day_in2 = input()
Min_In1 = input()
Min_In2 = input()
DAY_D,DAY_H = Day_HOU(Day_In1,Day_in2)
if DAY_H == '0':
    DAY_H = NEW_HOU(Min_In1,Min_In2)
DAY_M = GET_MIN(Min_In1,Min_In2)
TIME_Message = DAY_D+' '+DAY_H+':'+DAY_M
print(TIME_Message)