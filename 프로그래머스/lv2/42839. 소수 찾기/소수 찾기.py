from itertools import permutations

def is_prime(n):
    # 주어진 숫자 n이 2보다 작으면 소수가 아님
    if n < 2:
        return False
            
    # 2부터 제곱근까지의 숫자로 나누어 떨어지는지 확인하여 소수 여부 판별
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True
                   
def solution(numbers):
    answer = []
    numbers = list(numbers)
    
    # 숫자 조합의 길이에 따라 가능한 모든 조합 생성
    for i in range(1, len(numbers) + 1):
        perms = list(permutations(numbers, i)) 
        
        # 각 조합을 숫자로 변환하여 소수 여부 확인 후 answer 리스트에 추가
        for perm in perms:
            num = int(''.join(perm))
            
            if is_prime(num):
                answer.append(num)
    
    # 중복 제거를 위해 set으로 변환 후 길이 반환
    return len(set(answer))