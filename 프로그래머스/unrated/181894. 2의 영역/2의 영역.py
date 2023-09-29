def solution(arr):
    answer = []
    for i, v in enumerate(arr):
        if v == 2:
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    return arr[min(answer):max(answer)+1]