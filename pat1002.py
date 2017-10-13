#!/usr/bin/env python3
import math as ma
a=eval(input());
sum=0;
c=[];
l=[];
str1=['ling','yi','er','san','si','wu','liu','qi','ba','jiu'];
if a>=ma.pow(10,100):
        print(0);
else:
    b=str(a);
    for i in range(0,len(b)):
        c.append(b[i]);
        #print(c)
    for i in range(0,len(c)):
        sum=sum+eval(c[i]);
        i=i+1;
#print(sum);
while sum>0 and sum<=1000:
        n=int(sum%10);
        s=str1[n];
        l.append(s)
        #print(s,end='');
        sum=(sum-n)/10;
l.reverse()
for i in range(0,len(l)):
        if i<len(l)-1:
                print(l[i],end=' ');
        else:
                print(l[i],end='');

