#coding:utf-8

"""
2019.03.12.Tue.
<합의 제곱과 제곱의 합의 차>
...아니 이건 그냥 진짜로 구하면 되는 거잖아.
100개까지라서 오래 걸릴 것 같지도 않고.
실제로 원하는 건 이런 식으로 푸는 게 아닐 것 같은데
일단은.. 해보자.
"""
def sumSq(num):
    #합의 제곱
    sum=0
    for i in range(1, num+1):
        sum+=i

    return pow(sum, 2)

def sqSum(num):
    #제곱의 합
    sum=0
    for i in range(1, num+1):
        sum+=pow(i, 2)

    return sum

def main():
    num=100
    n1=sumSq(num)
    n2=sqSum(num)
    
    print(n1-n2)


if __name__=="__main__":
    main()
