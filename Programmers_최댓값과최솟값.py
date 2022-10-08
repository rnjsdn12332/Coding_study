import heapq
def solution(s):
    answer = ''
    array=s.split()
    heap1=[]
    heap2=[]
    for i in array :
        heapq.heappush(heap1, int(i))
        heapq.heappush(heap2, -1*int(i))
    
    answer+=str(heapq.heappop(heap1))
    answer+=" "
    answer+=str(-1*heapq.heappop(heap2))
    return answer
