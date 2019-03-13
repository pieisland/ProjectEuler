#coding:utf-8

"""
2019.03.13.Wed
왜.. commit이 안 되나 했더니만 이메일이 달라서 그런 거였다..
ㅎㅎ..;
git config --global user.name ""
git config --global user.email ""
설정을 하고
git config --list
로 확인을 해보자.. ^.^ 이제 제대로 되겠지??

<100!>
팩토리얼 문제. 팩토리얼의 모든 자릿수를 더하면 몇?
그냥.. 노가다로 하면 되는 것 아닌가?
"""

def main():
    num=100
    n=1
    for i in range(0, num):
        n=n*(i+1)
    
    sum=0
    numStr=str(n)    

    for i in range(0, len(numStr)):
        sum+=int(numStr[i])

    print(sum)

if __name__=="__main__":
    main()
