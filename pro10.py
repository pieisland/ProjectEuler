#coding:utf-8

import math

"""
2019.03.12.Tue.
<이백만 이해 소수의 합>
이것도 에라토스테네스의 체의 제곱근에 대한 걸 사용하면..
그나마 풀리는 편이긴 하지만 문제는...
20초가 넘는 시간이 걸림.
최적하는 어떻게 해야할까..?
"""

def findPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0:
            #print("It is not prime number")
            return 0
    
    #print("It is prime number")
    return 1

def main():
    num2=2
    sum=0
    while(num2<=2000000):  
        t=findPrime(num2)
        if t==1: sum+=num2
        num2+=1
    print(sum)

if __name__=="__main__":
    main()
