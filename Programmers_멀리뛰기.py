import math
def solution(n):
    #모두 1칸 뛸 경우의 수 1로 초기 설정으로 빼둠
    answer = 1
    
    #i는 1칸 뛰는 갯수
    for i in range(0,n) :
        #n-i의 값이 2로 나누어질 경우
        if (n-i)%2==0 :
            #1칸 뛰는 갯수와 2칸 뛰는 갯수가 모두 0이 아닐떄
            if i!=0 and (n-i)!=0:
                # 2칸 뛰는 갯수와 1칸 뛰는 갯수 합쳐서 몇번 뛰는지 cnt 변수에 설정
                cnt=((n-i)//2)+i
                  
                #팩토리얼로 계산 이때 주의 점은 /으로 나누는 것이 아닌 //로 나누어줄것(오버플로우 문제)
                answer+=math.factorial(cnt)//(math.factorial((n-i)//2)*math.factorial(i))
            else :
                #1칸 뛰는 갯수가 0이고 모두 2칸을 될 때
                answer+=1
    return int(answer)%1234567
