#문자열 입력
s=input()


while True:

    #수정사항 확인을 위한 cnt 변수 초기화
    cnt=0

    #문자열 길이가 1초과일경우
    if len(s) > 1 :
        for i in range(1,len(s)) :
            #연속 숫자 중복 확인
            if s[i-1]==s[i] :
                #연속 숫자 제거 후 s 수정
                s=s[:i-1]+s[i+1:]
                #수정 체크를 위한 cnt 올리기
                cnt+=1
                break

    else :
        break

    #연속 문자 없을 시 반복문 탈출
    if cnt==0 :
        break
#정답 출력
print("정답 : "+s)
    
