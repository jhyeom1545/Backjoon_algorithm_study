def solution(s):
    answer = 0
    arr = s.split(" ")
    for i, v in enumerate(arr):
        if v == 'Z':
            answer-=int(arr[i-1])
        else:
            answer+=int(v)
    return answer