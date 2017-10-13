#!/usr/bin/env python3
number=eval(input('a number:'));
A=[];
B=[];
C=[];
D=[];
while number!=0:
    name,schoolnumber,grade=map(str,input('name:,school:,grade:').split())
    A.append(name);
    B.append(schoolnumber);
    C.append(grade);
    number=number-1;
#print(A,B,C);

for i in range(0,len(C)):
    a=eval(C[i]);
    D.append(a);
    i=i+1;
b=max(D);
c=min(D);
for i in range(0,len(D)):
    if D[i]==b:
        n=i;
    else:
        i=i+1;
for i in range(0,len(D)):
    if D[i]==c:
        m=i;
    else:
        i=i+1;
#print(D);
print(A[n]+' '+B[n]);
print(A[m]+' '+B[m]);

