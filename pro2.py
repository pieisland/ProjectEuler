#coding:utf-8

"""
피보나치 수열에서짝수이면서 400만 이하인 모든 항을 더하기
"""

#동적 프로그래밍을 하자.

d=[]
for i in range(0, 100):
    d.append(0)

def fibonacci(x):
    if x==1: return 1
    if x==2: return 2
    if(d[x]!=0): return d[x]
    ans=fibonacci(x-1)+fibonacci(x-2)
    d[x]=ans
    return d[x]

x=fibonacci(7)
print(x)

idx = 1
sum = 0
x=0

#while문에서 continue를 쓸 때는 idx 값을 증가해야함을 잊지 말자
while(1):
    x=fibonacci(idx)
    if(x%2!=0):
        idx+=1
        continue
    if(x>4000000):
        break
    sum+=x
    idx+=1

print(sum)
print(idx) #신기하게도.. 4000000이라는 큰 숫자까지 가는 데 idx 값이 40도 안됨..
