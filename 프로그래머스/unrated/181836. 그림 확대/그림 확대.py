def solution(picture, k):
    answer = []
    for i in picture:
        val = ''
        for v in i:
            val+= v*k
        for i in range(k):
            answer.append(val)
        
    return answer