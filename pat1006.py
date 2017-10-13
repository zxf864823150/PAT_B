#!/usr/bin./env python3
a=int(input());
b=[];
#c=int(a);
a=str(a);
h=[];
if a[0]==0:
    a=a[1:];
else:
    a=a;
c=int(a);
if eval(a)==0:
    print(0);
else:
    for i in range(0,len(a)):
        n=c%10;
        c=(c-n)/10;
        d=int(n);
        b.append(d);
        i=i+1;
    e=range(1,b[0]+1);
    for i in range(0,len(e)):
        h.append(e[i]);
        i=i+1;
    g=''.join([str(i) for i in h]);
    if len(b)<3 and len(b)>1:
        print('S'*b[1]+g);
    if len(b)==1:
        print(g);
    else:
        print('B'*b[2]+'S'*b[1]+g);

