#coding:utf-8
import math

num=20

div=[2, 3, 5, 7, 11, 13, 17, 19]
a=[]

final=[0, 0, 0, 0, 0, 0, 0, 0]

#빈 리스트가 들어갈 수 있는지는 모르겠음
for i in range(0, num-1):
    a.append([0, 0, 0, 0, 0, 0, 0, 0])

def divide(num): #숫자를 소인수로 나눔
    idx=0
    dnum=num
    while(dnum!=1):
        if(dnum%div[idx]!=0):
            idx+=1
            continue
        dnum=int(dnum/div[idx])
        a[num-2][idx]+=1

for i in range(2, num+1):
    divide(i)

for i in range(0, len(final)):
    max=-1
    for j in range(0, num-1):
        if(max<a[j][i]):
            max=a[j][i]
    final[i]=max

answer=1
for i in range(0, len(final)):
    #print(final[i], end=" ")
    for j in range(0, final[i]):
        answer*=div[i]

print(answer)
    

