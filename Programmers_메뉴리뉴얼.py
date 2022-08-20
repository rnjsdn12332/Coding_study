from itertools import combinations
def solution(orders, course):
    answer = []
    #메뉴 조합을 담을 딕셔너리 생성
    all_menue=dict()
    for i in orders :
        for j in course:
            #코스메뉴갯수보다 주문메뉴갯수가 적으면 반복문 탈출
            if not len(i)>=j :
                break
            #코스메뉴갯수만큼 주문메뉴 조합한 리스트 생성
            tmp_list=list(combinations(i,j))
            for colabo in tmp_list :
                #조합된 메뉴 정렬하고 조인
                char=list(colabo)
                char.sort()
                char="".join(char)
                #딕셔너리에 메뉴가 등록안되어있다면 등록후 값 1로 설정
                if not char in all_menue.keys() :
                    all_menue[char]=1
                #등록되어있다면 갯수 1씩 추가
                else :
                    all_menue[char]=all_menue[char]+1
                
    for c in course :
        max_v=2
        #조합된 메뉴 중 중복갯수 최댓값 찾기
        for k,v in all_menue.items() :
            if len(k) == c :
                max_v=max(v, max_v)
        #제일 많이 조합된 메뉴 answer에 추가
        for k,v in all_menue.items() :
            if len(k)==c :
                if v==max_v :
                    answer.append(k)
    #정렬
    answer.sort()
    return answer
