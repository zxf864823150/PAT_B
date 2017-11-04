def FIND(a,b):
    if b in a:
        num_time = a.count(b)
        return int(b*num_time)
    else:
        return 0

INPUT_D = input().split(' ')
A = INPUT_D[0]
DA= INPUT_D[1]
B = INPUT_D[2]
DB = INPUT_D[3]
if int(A) <= 0 or int(A) >= pow(10,10) or int(B) <= 0 or \
    int(B) >= pow(10,10):
    print(None)
else:
    PA = FIND(A,DA)
    PB = FIND(B,DB)
    print(PA+PB)
