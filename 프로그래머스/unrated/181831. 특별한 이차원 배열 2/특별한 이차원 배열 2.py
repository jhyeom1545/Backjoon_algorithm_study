def solution(arr):
    answer = 1
    n = len(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != arr[j][i]:
                return 0
    return answer