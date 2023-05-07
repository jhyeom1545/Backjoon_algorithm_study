def solution(k, m, score):
    # k : 품질 점수
    # m : 상자에 들어가는 사과 개수
    # score : 주어진 사과의 개수
    answer = 0
    score.sort()
    result = 0
    num = len(score)%m
    for i in range(num):
        score.pop(0)
    for i in range(0,len(score),m):
        result += score[i]*m
    return result