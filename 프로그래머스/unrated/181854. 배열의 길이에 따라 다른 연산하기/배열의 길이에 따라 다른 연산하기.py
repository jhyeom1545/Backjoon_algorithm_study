def solution(arr, n):
    answer = []
    for i in range(0, len(arr)):
        if i % 2 == 1 and len(arr) % 2 == 0:
            answer.append(arr[i]+n)
        elif i % 2 == 0 and len(arr) % 2 == 1:
            answer.append(arr[i]+n)
        else:
            answer.append(arr[i])
    return answer