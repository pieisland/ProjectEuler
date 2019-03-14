#coding:utf-8

"""
2019.03.11.Thur
<제곱수 자릿수 모두 더하기>
그냥 하면 되는 문제.
"""

def main():
    num=1000
    n=pow(2, num)
    temp=str(n)

    sum=0
    for i in range(len(temp)):
        sum+=int(temp[i])
    print(sum)

if __name__=="__main__":
    main()
