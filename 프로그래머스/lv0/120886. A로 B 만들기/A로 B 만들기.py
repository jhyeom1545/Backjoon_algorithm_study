def solution(before, after):
    answer = 0
    be = sorted(before)
    af = sorted(after)
    if af == be:
        answer = 1
        
    return answer