
#숫자 입력
number=input()
#손뼉치는 횟수 저장할 변수
cnt=0

#주어진 숫자까지 1부터 차례대로 반복문
for n in range(1,int(number)+1) :
    #3, 6, 9 들어가있을때
    for num in str(n) :
        if "3" in num or "6" in num or "9" in num :
            #카운트 셈
            cnt+=1

print(cnt)
