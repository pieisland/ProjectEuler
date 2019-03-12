#coding:utf-8

import math

"""
2019.03.12.Tue.
<1001번쨰 소수>
딱 보니까 에라토스테네스의 체
인 것 같기는 한데 몇 번쨰의 소수를 구하라고 했기 때문에..
조금 애매한데..??
"""
def findPrime(n):

    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0:
            #print("It is not prime number")
            return 0
    
    #print("It is prime number")
    return 1


def main():
    a=[]

    cnt=1
    num=2
    while(cnt!=10001):
        num+=1
        n=findPrime(num)
        if n==1: cnt+=1
        
    print(num)
    
if __name__=="__main__":
    main()
