money=int(input())
result=[]
#나눈 몫을 result에 담고 나눈후 나머지를 그 다음 화폐단위에 넘기는식
result.append(money//50000)
money%=50000
result.append(money//10000)
money%=10000
result.append(money//5000)
money%=5000
result.append(money//1000)
money%=1000
result.append(money//500)
money%=500
result.append(money//100)
money%=100
result.append(money//50)
money%=50
result.append(money//10)
money%=10
result.append(money//1)
money%=1
print(result)
