from collections import deque
def solution(rc, operations):
    answer = [[]]
    q=deque(rc)
    r_len=len(rc)
    c_len=len(rc[0])
    rows = deque(deque(row[1:-1]) for row in rc)
        
    out_cols = [deque(rc[r][0] for r in range(r_len)),
                deque(rc[r][c_len - 1] for r in range(r_len))] 
    def shift() :
        rows.appendleft(rows.pop())
        out_cols[0].appendleft(out_cols[0].pop())
        out_cols[1].appendleft(out_cols[1].pop())
        
    def rotation() :
        #왼쪽 첫 열 이동
        rows[0].appendleft(out_cols[0].popleft())
        #위 첫 행에서 오른족 열로 이동
        out_cols[1].appendleft(rows[0].pop())
        #왼쪽 열에서 아래 맨 뒤 행 이동
        rows[r_len-1].append(out_cols[1].pop())
        #맨 아래 행에서 왼쪽 열로 이동
        out_cols[0].append(rows[r_len-1].popleft())
         
    
    for oper in operations :
        if "S" in oper :
            shift()
        else :
            rotation()
    answer=[]
    for r in range(r_len) :
        temp=[]
        temp.append(out_cols[0][r])
        temp.extend(rows[r])
        temp.append(out_cols[1][r])
        answer.append(temp)
    return answer
