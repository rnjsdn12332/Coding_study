#포비와 크롱이 페이지 번호 담긴 배열 받기
pobi=list(input().split())
crong=list(input().split())

#왼쪽 페이지 오른쪽 페이지가 잘들어갔는지 확인
def check(arr) :
    if int(arr[0])%2==1 and int(arr[1])==int(arr[0])+1 :
        return True
    else :
        return False


# 숫자끼리 더한것과 곱한것 중 큰 값 반환
def find_big(x) :
    val=1
    for v in x :
        val*=int(v)
    val2=0
    for v in x :
        val2+=int(v)
    return max(val, val2)

#두 수 중 큰 값 반환
def compare(a, b) :
    if a>b :
        return a
    elif a<=b :
        return b

#포비와 크롱 승부 반환
def result(a,b) :
    if a>b :
        return 1
    elif a<b :
        return 2
    else :
        return 0


def solution(pobi, crong) :

    #규칙대로 페이지번호가 잘 들어가있는 경우
    if check(pobi) and check(crong) :

        #a는 포비 b는 크롱의 값
        a=compare(find_big(pobi[0]),find_big(pobi[1]))
        b=compare(find_big(crong[0]),find_big(crong[1]))

        #승부 반환하는 함수 호출
        print(result(a,b))
    
    #규칙대로 페이지 번호가 들어있지 않은 경우
    else :
        print(-1)

solution(pobi, crong)
