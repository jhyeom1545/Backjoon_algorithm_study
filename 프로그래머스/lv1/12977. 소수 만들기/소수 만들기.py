from itertools import combinations
def is_prime(num):
    if num < 2: # 1보다 작으면 false 소수가 아님
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    for i in combinations(nums,3):
        if is_prime(sum(i)):
            answer+=1
    return answer        
    
