#coding:utf-8

"""
1000보다 작은 자연수 중 3 또는 5의 배수를 모두 더하기
"""

a=[]

for i in range(1, 1000):
    if i%3==0 or i%5==0:
        a.append(i)
    #if i%3==0:
    #    a.append(i)
    #if i%5==0 and i%15!==0:
    #    a.append(i)

sum=0
for i in range(0, len(a)):
    sum+=a[i]

print(sum)

#공배수에 대해서 어렵게 생각하지 않아도 되는 거였다. 그냥 or로 하면 되네..

