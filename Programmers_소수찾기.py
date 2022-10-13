def find(x) :
        if x==0 or x==1 :
            return False
        for i in range(2, x) :
            if x%i ==0 :
                return False
        return True
    
def search_numbers(numbers, i, chk_nums, prime_list):
    for j in numbers:
        num = i + j
        rem = numbers.replace(j, '', 1)
        if int(num) not in chk_nums:
            chk_nums.append(int(num))
            if find(int(num)):
                prime_list.append(int(num))
        if rem:
            search_numbers(rem, num, chk_nums, prime_list)

def solution(numbers):
    answer = 0
    chk_nums = []
    prime_list = []
    for i in numbers:
        if int(i) not in chk_nums:
            chk_nums.append(int(i))
            if find(int(i)):
                prime_list.append(int(i))
        rem = numbers.replace(i, '', 1)
        search_numbers(rem, i, chk_nums, prime_list)
    answer = len(prime_list)
    print(chk_nums, prime_list)
    return answer
