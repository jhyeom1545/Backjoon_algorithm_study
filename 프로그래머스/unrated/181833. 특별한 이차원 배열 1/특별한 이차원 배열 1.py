def solution(n):
    answer = []
    if n == 1:
        return [[1]]
    for i in range(n):
        answer.append([])
        for j in range(n):
            if i == j:
                answer[i].append(1)
            else:
                answer[i].append(0)
    return answer