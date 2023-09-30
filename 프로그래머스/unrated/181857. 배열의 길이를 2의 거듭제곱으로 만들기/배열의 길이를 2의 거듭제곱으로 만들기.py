# def solution(arr):
#     pow2 = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512]
#     for i in pow2:
#         if len(arr) < i:
#             for i in range(i-len(arr)):
#                 arr.append(0)
#             return arr
#         elif len(arr) == i:
#             return arr
#         elif len(arr) == 1
        
def solution(arr):
    l = len(arr)
    while bin(l).count('1') != 1: #이 조건을 만족하면 l은 2의 거듭제곱입니다.
        l += l & (-l) # l과 l의 보수를 and 연산을 합니다. 이 연산을 반복하면 2의 거듭제곱 형태가 됩니다.
    return arr + [0] * (l - len(arr))