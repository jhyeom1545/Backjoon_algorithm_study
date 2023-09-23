def solution(binomial):
    answer = 0
    arr = binomial.split(" ")
    for i in arr:
        if '+' in arr:
            answer = int(arr[0]) + int(arr[2])
            return answer
        if '-' in arr:
            answer = int(arr[0]) - int(arr[2])
            return answer
        if '*' in arr:
            answer = int(arr[0]) * int(arr[2])
            return answer