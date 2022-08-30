def rotate_a_matrix_by_90_degree(a) :
    n=len(a)
    m=len(a[0])
    result=[[0]*n for _ in range(m)]
    for i in range(n) :
        for j in range(m) :
            result[j][n-i-1]=a[i][j]
    return result
#자물쇠에 해당하는 부분이 모두 1인지 확인
def check(new_lock) :
    lock_length=len(new_lock)//3
    for i in range(lock_length, lock_length*2) :
        for j in range(lock_length, lock_length*2) :
            if new_lock[i][j]!=1 :
                return False
    return True

def solution(key, lock):
    answer = True
    n=len(lock)
    m=len(key)
    
    new_lock=[[0]*(n*3) for _ in range(n*3)]
    
    #새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n) :
        for j in range(n) :
            new_lock[i+n][j+n]=lock[i][j]
    
    for rotation in range(4) :
        key=rotate_a_matrix_by_90_degree(key) #열쇠 회전
        for x in range(n*2) :
            for y in range(n*2) :
                #자물쇠에 열쇠 끼워넣기
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x+i][y+j]+=key[i][j]
                        
                #새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock):
                    return True
                #자물쇠에 열쇠를 다시 빼기
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x+i][y+j]-=key[i][j]
        
    return Falseㅍ
