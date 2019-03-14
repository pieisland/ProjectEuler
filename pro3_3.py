#coding:utf-8

"""
2019.03.14.Thu
<소인수분해>
효율적인 버전.
다른 분이 푸신 걸 보고 다시 풀어봄
"""

def primeNumber(n):
    """
    소인수분해하는 함수
    n이 큰 수라도, 나눈 결과로 다시 되기 떄문에 빠르게 수행이 되는 듯.
    result 자체에 중복되는 소수가 들어가지 않게 in 을 추가로 더 넣어봄.
    """

    i=2
    result=[]
    while(i<=n):
        if(n%i==0):
            n=n//i
            if i not in result:
                result.append(i)
        else:
            i+=1
    return result

def main():
    n=600851475143
    
    tmp=primeNumber(n)
    print(tmp)
    print(max(tmp))

if __name__=="__main__":
    main()
