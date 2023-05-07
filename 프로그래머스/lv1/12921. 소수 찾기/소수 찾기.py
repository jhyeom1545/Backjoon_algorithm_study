# def solution(n):
#     # 1부터 n까지 모든 수를 적는다.
#     nums = [True] * (n+1)
#     # 아직 지워지지 않은 수 중에서 가장 작은 수를 찾는다.
#     for i in range(2, int(n**0.5)+1):
#         if nums[i]:
#             # 그 수는 소수이다.
#             # 이제 그 수의 배수를 모두 지운다.
#             for j in range(i*2, n+1, i):
#                 nums[j] = False
#     # 아직 지워지지 않은 수가 있으면, 2번으로 간다.
#     return nums[2:].count(True)

def solution(n):
    nums = [True] * (n+1)
    print(int(n**0.5)+1)
    for i in range(2, int(n**0.5)+1):
        if nums[i]:
            for j in range(i*2, n+1, i):
                nums[j] = False
    return nums[2:].count(True)
