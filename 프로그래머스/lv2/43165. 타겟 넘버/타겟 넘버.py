# def solution(numbers, target):
#     answer = DFS(numbers, target, 0)
#     return answer

# def DFS(numbers, target, depth):
#     # 종료 조건: 모든 숫자에 대해 탐색을 완료한 경우
#     if depth == len(numbers):
#         # 타겟 넘버와 일치하는 경우 1을 반환, 아닌 경우 0을 반환
#         if sum(numbers) == target:
#             return 1
#         else:
#             return 0
#     else:
#         # 현재 숫자를 더하는 경우와 빼는 경우를 각각 재귀 호출
#         result = 0
#         result += DFS(numbers, target, depth + 1)  # 현재 숫자를 그대로 더하는 경우
#         numbers[depth] *= -1  # 현재 숫자를 반전하여 빼는 경우
#         result += DFS(numbers, target, depth + 1)
#         numbers[depth] *= -1  # 원래 숫자로 되돌리기
#         return result

def solution(numbers, target):
    # 메모이제이션을 위한 딕셔너리 생성
    memo = {}
    answer = DFS(numbers, target, 0, memo)
    return answer

def DFS(numbers, target, depth, memo):
    if depth == len(numbers):
        if target == 0:  # 타겟 넘버가 0이 되는 경우 1을 반환
            return 1
        else:
            return 0
    else:
        # 메모이제이션을 확인하여 계산 결과가 저장되어 있는 경우 반환
        if (depth, target) in memo:
            return memo[(depth, target)]
        
        # 현재 숫자를 더하거나 빼는 경우를 재귀 호출하여 계산
        result = DFS(numbers, target - numbers[depth], depth + 1, memo)  # 현재 숫자를 더하는 경우
        result += DFS(numbers, target + numbers[depth], depth + 1, memo)  # 현재 숫자를 빼는 경우
        
        # 계산 결과를 메모이제이션에 저장
        memo[(depth, target)] = result
        return result
