A,B = list(map(eval,input().split(' ')))
if A >= pow(10,1000) or B >= 10 or A <=0 or B <= 0:
    print(None)
else:
    Q = A//B
    R = A%B
print('%d '%Q+'%d'%R)