#coding:utf-8

"""
2019.03.14.Thur
<소인수분해>
말그대로 소인수 분해를 해서 풀면 되는 문제를.. 어렵게 풀었음.
소수를 일일이 구할 필요 없음.
"""
import math

def isPrime(num):
    for i in range(2, num):
        if num%i==0:
            return 0
    return 1

def main():

    """
    내 생각은 일단 소수를 다 구한 후에
    소수들을 크기 순으로 저장을 한 후
    맨 뒤에서부터 확인을 해서 숫자%소수==0
    인 애를 출력하는 것.
    근데 시간 오래 걸림
    """

    num=600851475143
    num2=int(math.sqrt(num))
    a=[]
    for i in range(0, num2+1):
        a.append(i)
    a[1]=0

    for i in range(2, num2+1):
        j=i+i
        while(j<num2+1):
            a[j]=0
            j+=i
    
    prime=[]
    for i in range(0, num2+1):
        if a[i]!=0:
            prime.append(i)
    #print(prime)

    idx=-1
    
    while(1):
        if num%prime[idx]==0:
            print(prime[idx])
            break
        #prime.remove(prime[-1])
        idx-=1

def main2():
    #num=600851475143
    num=13195
    num2=int(math.sqrt(num))
    
    result=0

    for i in range(2, num2+1):
        n=isPrime(i)
        if num%i==0 and n==1:
            result=i

    print(result)
    
if __name__=="__main__":
    main()
