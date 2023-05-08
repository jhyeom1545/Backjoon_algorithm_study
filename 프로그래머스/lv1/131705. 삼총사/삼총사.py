# from itertools import combinations

# def solution(numbers):
#     count = 0
#     for comb in combinations(numbers, 3):
#         if sum(comb) == 0:
#             count += 1
#     return count

# from itertools imxport *
# def solution(numbers):
#     answer = 0
#     for com in combinations(numbers, 3):
#         if sum(com)==0:
#             answer+=1
#     return answer
        
def solution(numbers):
    n = len(numbers)
    answer = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if numbers[i] + numbers[j] + numbers[k] == 0:
                    answer += 1
    return answer

def solution(numbers):
    answer = 0
    for i in range(len(numbers)-2):
        for j in range(i+1,len(numbers)-1):
            for k in range(j+1,len(numbers)):
                if numbers[i]+numbers[j]+numbers[k]==0:
                    answer +=1
    return answer